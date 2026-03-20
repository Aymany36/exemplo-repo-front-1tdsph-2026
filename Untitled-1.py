def calcular_conta_energia():
    print("--- Calculadora de Conta de Energia 2026 ---")
    
    try:
        # Recebe o consumo do usuário
        consumo = float(input("Digite o consumo em kWh: "))
        
        # Define o valor por kWh com base nas faixas
        if consumo < 150:
            valor_kwh = 0.75
        elif consumo <= 500:
            valor_kwh = 0.95
        else:
            valor_kwh = 1.20
            
        # Cálculo base
        valor_calculado = consumo * valor_kwh
        taxa_minima = 45.00
        
        # Aplicação da Regra de Negócio: Taxa Mínima (Disponibilidade)
        valor_final = max(valor_calculado, taxa_minima)
        
        # Exibição dos resultados
        print(f"\nResultado do Processamento:")
        print(f"Consumo informado: {consumo} kWh")
        print(f"Valor calculado por consumo: R$ {valor_calculado:.2f}")
        
        if valor_calculado < taxa_minima:
            print(f"Atenção: Valor abaixo do mínimo. Aplicada Taxa de Disponibilidade (R$ {taxa_minima:.2f})")
        
        print(f"--- VALOR TOTAL A PAGAR: R$ {valor_final:.2f} ---")

    except ValueError:
        print("Erro: Por favor, insira um valor numérico válido para o consumo.")
