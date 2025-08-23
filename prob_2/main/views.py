# main/views.py

import requests
import json
from django.shortcuts import render
from django.conf import settings
from datetime import datetime, timedelta

def index(request):
    context = {
        'currencies': {},
        'converted_amount': None,
        'from_amount': '',
        'from_curr': '',
        'to_curr': '',
        'chart_data': None,
    }
    api_key = settings.API_KEY

    # Fetch the list of supported currency codes
    try:
        codes_url = f'https://v6.exchangerate-api.com/v6/{api_key}/codes'
        response = requests.get(codes_url)
        response.raise_for_status()
        data = response.json()

        processed_currencies = {}
        if data.get('result') == 'success':
            for code_list in data.get('supported_codes', []):
                processed_currencies[code_list[0]] = {'description': code_list[1]}
            context['currencies'] = processed_currencies
        else:
            context['error'] = 'Could not retrieve currency codes.'
            return render(request, 'main/index.html', context)

    except requests.exceptions.RequestException as e:
        context['error'] = f"Could not fetch currencies: {e}"
        return render(request, 'main/index.html', context)

    # Handle the conversion form submission
    if request.method == 'POST':
        from_amount_str = request.POST.get('from_amount', '0').strip()
        from_curr = request.POST.get('from_curr')
        to_curr = request.POST.get('to_curr')

        context.update({
            'from_amount': from_amount_str,
            'from_curr': from_curr,
            'to_curr': to_curr,
        })

        try:
            from_amount = float(from_amount_str)
        except ValueError:
            context['error'] = 'Please enter a valid number for the amount.'
            return render(request, 'main/index.html', context)

        # Make the API call for the conversion
        try:
            pair_url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_curr}/{to_curr}/{from_amount}'
            conversion_response = requests.get(pair_url)
            conversion_response.raise_for_status()
            conversion_data = conversion_response.json()

            if conversion_data.get('result') == 'success':
                context['converted_amount'] = conversion_data.get('conversion_result')
                
                # --- DEFINITIVE FIX for historical data ---
                try:
                    today = datetime.now()
                    thirty_days_ago = today - timedelta(days=30)
                    start_date = thirty_days_ago.strftime('%Y-%m-%d')
                    
                    history_url = f'https://api.frankfurter.app/{start_date}..{today.strftime("%Y-%m-%d")}?from={from_curr}&to={to_curr}'
                    history_response = requests.get(history_url)
                    history_response.raise_for_status()
                    history_data = history_response.json()
                    
                    if 'rates' in history_data and isinstance(history_data['rates'], dict):
                        rates = history_data.get('rates', {})
                        sorted_rates = sorted(rates.items())
                        
                        final_labels = []
                        final_series = []

                        for date, rate_values in sorted_rates:
                            if isinstance(rate_values, dict) and to_curr in rate_values:
                                final_labels.append(date)
                                final_series.append(rate_values[to_curr])
                        
                        if final_labels and final_series:
                            context['chart_data'] = json.dumps({
                                'labels': final_labels,
                                'series': final_series,
                                'from_curr': from_curr,
                                'to_curr': to_curr
                            })

                except Exception as chart_e:
                    print(f"DEBUG: Could not fetch or process chart data: {chart_e}")
                # --- END of definitive fix ---

            else:
                context['error'] = conversion_data.get('error-type', 'Could not perform conversion.')

        except requests.exceptions.RequestException as e:
            context['error'] = f"API request failed: {e}"

    return render(request, 'main/index.html', context)