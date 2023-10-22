# views.py

from django.shortcuts import render
import joblib
regressor=model = joblib.load('random_forest_model.pkl')

def predict(request):
    AMBASSADOR=0
    AUDI=0
    BENTLEY=0
    BMW=0
    CHEVROLET=0
    DATSUN=0
    FIAT=0
    FORCE=0
    FORD=0
    HONDA=0
    HYUNDAI=0
    ISUZU=0
    JAGUAR=0
    JEEP=0
    LAMBORGHINI=0
    LAND=0
    MAHINDRA=0
    MARUTI=0
    MERCEDES=0
    MINI=0
    MITSUBISHI=0
    NISSAN=0
    PORSCHE=0
    RENAULT=0
    SKODA=0
    TATA=0
    TOYOTA=0
    VOLKSWAGEN=0
    VOLVO=0

    #LOCATION
    Ahmedabad=0
    Bangalore=0
    Chennai=0
    Pune=0
    Mumbai=0
    Coimbatore=0
    Hyderabad=0
    Jaipur=0
    Kochi=0
    Kolkata=0
    Delhi=0

    #FUEL
    Diesel=0
    LPG=0
    Petrol=0
    CNG=0

    #TRANSMISSION
    Manual=0
    if request.method == 'POST':
        name = request.POST.get('Brand')
        if name == 'AUDI':
            AUDI=1
        elif name == 'BENTLEY':
            BENTLEY=1    
        elif name == 'BMW':
            BMW=1    
        elif name == 'CHEVROLET':
            CHEVROLET=1
        elif name == 'DATSUN':
            DATSUN=1    
        elif name == 'FIAT':
            FIAT=1    
        elif name == 'FORCE':
            FORCE=1
        elif name == 'FORD':
            FORD=1
        elif name == 'HONDA':
            HONDA=1
        elif name == 'HYUNDAI':
            HYUNDAI=1
        elif name == 'ISUZU':
            ISUZU=1            
        elif name == 'JAGUAR':
            JAGUAR=1
        elif name == 'JEEP':
            JEEP=1
        elif name == 'LAMBORGHINI':
            LAMBORGHINI=1
        elif name == 'LAND':
            LAND=1    
        elif name == 'MAHINDRA':
            MAHINDRA=1    
        elif name == 'MARUTI':
            MARUTI=1    
        elif name == 'MERCEDES-BENZ':
            MERCEDES=1    
        elif name == 'MINI':
            MINI=1    
        elif name == 'MITSUBUSHI':
            MITSUBISHI=1    
        elif name == 'NISSAN':
            NISSAN=1    
        elif name == 'PORSCHE':
            PORSCHE=1    
        elif name == 'RENAULT':
            RENAULT=1            
        elif name == 'SKODA':
            SKODA=1    
        elif name == 'TATA':
            TATA=1    
        elif name == 'TOYOTA':
            TOYOTA=1    
        elif name == 'VOLKSWAGEN':
            VOLKSWAGEN=1    
        elif name == 'VOLVO':
            VOLVO=1    
        else:
            AMBASSADOR=1
        loc = request.POST.get('Location')
        if loc=='Bangalore':
            Bangalore=1    
        elif loc=='Chennai':
            Chennai=1    
        elif loc=='Pune':
            Pune=1    
        elif loc=='Mumbai':
            Mumbai=1    
        elif loc=='Coimbatore':
            Coimbatore=1
        elif loc=='Hyderabad':
            Hyderabad=1   
        elif loc=='Jaipur':
            Jaipur=1  
        elif loc=='Kochi':
            Kochi=1
        elif loc=='Kolkata':
            Kolkata=1
        elif loc=='Delhi':
            Delhi=1
        else:
            Ahmedabad=1
        fuel = request.POST.get('Fuel')
        if fuel=='Diesel':
            Diesel=1    
        elif fuel=='Petrol':
            Petrol=1    
        elif fuel=='LPG':
            LPG=1    
        else:
            CNG=1
        trans = request.POST.get('Transmission')
        if trans == 'Manual':
            Manual=1
        year = float(request.POST.get('Year'))
        kms = float(request.POST.get('Kms'))
        owner = float(request.POST.get('Owner'))
        mileage = float(request.POST.get('Mileage'))
        engine = float(request.POST.get('Engine'))
        power = float(request.POST.get('Power'))
        seats = float(request.POST.get('Seats'))

        features = [
    year, kms, owner, mileage, engine, power, seats,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 1.0
]
        Price = regressor.predict([features])
    
        output=Price
        print(output)

        # Perform the prediction using your trained model here
        # Example: Price = regressor.predict(...)
        Price = 0.0  # Replace with your prediction logic

        return render(request, 'predict.html', {'prediction': output})

    return render(request, 'predict.html')
