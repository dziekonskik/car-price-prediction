premium_brands = {"Mercedes-Benz", "BMW", "Audi", "Porsche", "Lexus", "Jaguar", "Tesla", "Maserati", "Ferrari", "Bentley", "Rolls-Royce", "Aston Martin", "Lamborghini"}
budget_brands = {"Dacia", "Fiat", "Renault", "Opel", "Peugeot", "Škoda", "Hyundai", "Kia", "Daewoo", "Suzuki"}

def categorize_brand(brand):
    """
    Przypisuje markę pojazdu do jednej z kategorii: Premium, Budżetowe, Średnie.
    
    :param brand: Nazwa marki samochodu
    :return: Kategoria jako string (Premium, Budżetowe, Średnie)
    """
    if brand in premium_brands:
        return "Premium"
    elif brand in budget_brands:
        return "Budżetowe"
    else:
        return "Średnie"
