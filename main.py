from fastapi import FastAPI, Security, HTTPException, status
from fastapi.security import APIKeyHeader
from typing import List

app = FastAPI(title="Agri-Input Tracking API")

# --- 1. USALAMA (API KEY) ---
# Huu ndio ufunguo wako. Mtu akiutumia huu tu ndio atapata data.
API_KEY = "agri_secure_2026_key"
api_key_header = APIKeyHeader(name="X-API-KEY")

def validate_api_key(api_key: str = Security(api_key_header)):
    if api_key == API_KEY:
        return api_key
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Access Denied: Invalid API Key. Please provide a valid key in the header."
    )

# --- 2. DATA ZA BIDHAA (40 ITEMS) ---
data_store = {
    "seeds": [
        # --- 10 EXPIRED SEEDS ---
        {"id": 1, "product_name": "Hybrid Maize H1", "batch_number": "B001", "category": "Cereals", "manufacturer": "SeedCo", "mfg_date": "2023-01-10", "exp_date": "2024-01-10", "brand": "SuperHarvest", "qr_code": "https://qr.io/s/B001"},
        {"id": 2, "product_name": "Soybean Pro", "batch_number": "B002", "category": "Legumes", "manufacturer": "Pioneer", "mfg_date": "2022-11-15", "exp_date": "2023-11-15", "brand": "GreenGrow", "qr_code": "https://qr.io/s/B002"},
        {"id": 3, "product_name": "Sunflower XL", "batch_number": "B003", "category": "Oil Seeds", "manufacturer": "Pannar", "mfg_date": "2023-02-20", "exp_date": "2024-02-20", "brand": "SunBright", "qr_code": "https://qr.io/s/B003"},
        {"id": 4, "product_name": "Rice King", "batch_number": "B004", "category": "Cereals", "manufacturer": "AgroBase", "mfg_date": "2023-03-05", "exp_date": "2024-03-05", "brand": "DeltaPure", "qr_code": "https://qr.io/s/B004"},
        {"id": 5, "product_name": "Wheat Prime", "batch_number": "B005", "category": "Cereals", "manufacturer": "SeedCo", "mfg_date": "2022-12-01", "exp_date": "2023-12-01", "brand": "MillMax", "qr_code": "https://qr.io/s/B005"},
        {"id": 6, "product_name": "Sorghum Red", "batch_number": "B006", "category": "Cereals", "manufacturer": "Advanta", "mfg_date": "2023-01-25", "exp_date": "2024-01-25", "brand": "DryTough", "qr_code": "https://qr.io/s/B006"},
        {"id": 7, "product_name": "Bean Star", "batch_number": "B007", "category": "Legumes", "manufacturer": "Kenya Seeds", "mfg_date": "2023-04-10", "exp_date": "2024-04-10", "brand": "NutriBean", "qr_code": "https://qr.io/s/B007"},
        {"id": 8, "product_name": "Barley Gold", "batch_number": "B008", "category": "Cereals", "manufacturer": "Syngenta", "mfg_date": "2022-09-18", "exp_date": "2023-09-18", "brand": "BrewBest", "qr_code": "https://qr.io/s/B008"},
        {"id": 9, "product_name": "Peanut Max", "batch_number": "B009", "category": "Oil Seeds", "manufacturer": "Bayer", "mfg_date": "2023-05-12", "exp_date": "2024-05-12", "brand": "NutOil", "qr_code": "https://qr.io/s/B009"},
        {"id": 10, "product_name": "Millet Fast", "batch_number": "B010", "category": "Cereals", "manufacturer": "SeedCo", "mfg_date": "2023-02-14", "exp_date": "2024-02-14", "brand": "Savanna", "qr_code": "https://qr.io/s/B010"},
        
        # --- 10 ACTIVE SEEDS (NOT EXPIRED) ---
        {"id": 11, "product_name": "Maize DK8031", "batch_number": "B011", "category": "Cereals", "manufacturer": "Bayer", "mfg_date": "2025-10-01", "exp_date": "2027-10-01", "brand": "Dekalb", "qr_code": "https://qr.io/s/B011"},
        {"id": 12, "product_name": "Veggie Tomato", "batch_number": "B012", "category": "Vegetables", "manufacturer": "Monsanto", "mfg_date": "2026-01-15", "exp_date": "2028-01-15", "brand": "FreshGard", "qr_code": "https://qr.io/s/B012"},
        {"id": 13, "product_name": "Cabbage Round", "batch_number": "B013", "category": "Vegetables", "manufacturer": "EastWest", "mfg_date": "2025-12-20", "exp_date": "2027-12-20", "brand": "FarmLink", "qr_code": "https://qr.io/s/B013"},
        {"id": 14, "product_name": "Onion Red S1", "batch_number": "B014", "category": "Vegetables", "manufacturer": "Syngenta", "mfg_date": "2026-02-01", "exp_date": "2028-02-01", "brand": "BulbBest", "qr_code": "https://qr.io/s/B014"},
        {"id": 15, "product_name": "Cotton White", "batch_number": "B015", "category": "Fiber", "manufacturer": "Mahyco", "mfg_date": "2025-11-10", "exp_date": "2027-11-10", "brand": "TexSeed", "qr_code": "https://qr.io/s/B015"},
        {"id": 16, "product_name": "Potato Spud", "batch_number": "B016", "category": "Tubers", "manufacturer": "EuroPlant", "mfg_date": "2026-03-05", "exp_date": "2028-03-05", "brand": "TuberTech", "qr_code": "https://qr.io/s/B016"},
        {"id": 17, "product_name": "Chili Hot", "batch_number": "B017", "category": "Vegetables", "manufacturer": "Namdhari", "mfg_date": "2026-01-30", "exp_date": "2028-01-30", "brand": "SpiceUp", "qr_code": "https://qr.io/s/B017"},
        {"id": 18, "product_name": "Lentil Green", "batch_number": "B018", "category": "Legumes", "manufacturer": "AgroGlobal", "mfg_date": "2025-09-15", "exp_date": "2027-09-15", "brand": "SoilFix", "qr_code": "https://qr.io/s/B018"},
        {"id": 19, "product_name": "Watermelon Big", "batch_number": "B019", "category": "Fruits", "manufacturer": "Sakata", "mfg_date": "2026-04-10", "exp_date": "2028-04-10", "brand": "JuicySweet", "qr_code": "https://qr.io/s/B019"},
        {"id": 20, "product_name": "Carrot Sweet", "batch_number": "B020", "category": "Vegetables", "manufacturer": "Bejo", "mfg_date": "2026-02-20", "exp_date": "2028-02-20", "brand": "OrangeGold", "qr_code": "https://qr.io/s/B020"},
    ],
    "fertilizers": [
        # --- 10 EXPIRED FERTILIZERS ---
        {"id": 1, "product_name": "NPK 17:17:17", "batch_number": "F001", "category": "Multi", "manufacturer": "Yara", "mfg_date": "2022-01-01", "exp_date": "2023-01-01", "brand": "Mila", "qr_code": "https://qr.io/f/F001"},
        {"id": 2, "product_name": "DAP Planting", "batch_number": "F002", "category": "Phosphate", "manufacturer": "OCP", "mfg_date": "2022-05-10", "exp_date": "2023-05-10", "brand": "PowerGrow", "qr_code": "https://qr.io/f/F002"},
        {"id": 3, "product_name": "UREA 46%", "batch_number": "F003", "category": "Nitrogen", "manufacturer": "Indorama", "mfg_date": "2022-03-20", "exp_date": "2023-03-20", "brand": "LeafGreen", "qr_code": "https://qr.io/f/F003"},
        {"id": 4, "product_name": "CAN Booster", "batch_number": "F004", "category": "Nitrogen", "manufacturer": "Yara", "mfg_date": "2021-11-15", "exp_date": "2022-11-15", "brand": "NitraFast", "qr_code": "https://qr.io/f/F004"},
        {"id": 5, "product_name": "MOP Potash", "batch_number": "F005", "category": "Potassium", "manufacturer": "K+S", "mfg_date": "2022-06-05", "exp_date": "2023-06-05", "brand": "RootStrong", "qr_code": "https://qr.io/f/F005"},
        {"id": 6, "product_name": "TSP Super", "batch_number": "F006", "category": "Phosphate", "manufacturer": "AgroChem", "mfg_date": "2022-02-12", "exp_date": "2023-02-12", "brand": "TripleMax", "qr_code": "https://qr.io/f/F006"},
        {"id": 7, "product_name": "SA Sulphate", "batch_number": "F007", "category": "Sulphur", "manufacturer": "IFFCO", "mfg_date": "2022-04-18", "exp_date": "2023-04-18", "brand": "SulphiFix", "qr_code": "https://qr.io/f/F007"},
        {"id": 8, "product_name": "Organic Mix", "batch_number": "F008", "category": "Organic", "manufacturer": "BioFarm", "mfg_date": "2022-08-30", "exp_date": "2023-08-30", "brand": "EcoEarth", "qr_code": "https://qr.io/f/F008"},
        {"id": 9, "product_name": "Liquid Bloom", "batch_number": "F009", "category": "Foliar", "manufacturer": "VegGrow", "mfg_date": "2022-07-22", "exp_date": "2023-07-22", "brand": "Flowa", "qr_code": "https://qr.io/f/F009"},
        {"id": 10, "product_name": "Zinc Boost", "batch_number": "F010", "category": "Micronutrient", "manufacturer": "Tims", "mfg_date": "2022-01-25", "exp_date": "2023-01-25", "brand": "MicroGrow", "qr_code": "https://qr.io/f/F010"},
        
        # --- 10 ACTIVE FERTILIZERS (NOT EXPIRED) ---
        {"id": 11, "product_name": "YaraMila Winner", "batch_number": "F011", "category": "Multi", "manufacturer": "Yara", "mfg_date": "2026-01-01", "exp_date": "2028-01-01", "brand": "Winner", "qr_code": "https://qr.io/f/F011"},
        {"id": 12, "product_name": "DAP Plus", "batch_number": "F012", "category": "Phosphate", "manufacturer": "ETG", "mfg_date": "2026-03-10", "exp_date": "2028-03-10", "brand": "Falcon", "qr_code": "https://qr.io/f/F012"},
        {"id": 13, "product_name": "Calcium Nitrate", "batch_number": "F013", "category": "Nitrogen", "manufacturer": "SQM", "mfg_date": "2026-02-15", "exp_date": "2028-02-15", "brand": "Qrop", "qr_code": "https://qr.io/f/F013"},
        {"id": 14, "product_name": "Humic Acid", "batch_number": "F014", "category": "Soil Conditioner", "manufacturer": "HuminTech", "mfg_date": "2026-04-05", "exp_date": "2029-04-05", "brand": "BlackGold", "qr_code": "https://qr.io/f/F014"},
        {"id": 15, "product_name": "NPK 20:10:10", "batch_number": "F015", "category": "Multi", "manufacturer": "Indorama", "mfg_date": "2025-12-01", "exp_date": "2027-12-01", "brand": "Granul", "qr_code": "https://qr.io/f/F015"},
        {"id": 16, "product_name": "Magnesium Sul", "batch_number": "F016", "category": "Secondary", "manufacturer": "K+S", "mfg_date": "2026-01-20", "exp_date": "2028-01-20", "brand": "EpsomAgri", "qr_code": "https://qr.io/f/F016"},
        {"id": 17, "product_name": "Foliar Feed B", "batch_number": "F017", "category": "Foliar", "manufacturer": "Osho", "mfg_date": "2026-03-22", "exp_date": "2028-03-22", "brand": "EasyGrow", "qr_code": "https://qr.io/f/F017"},
        {"id": 18, "product_name": "Compost Pro", "batch_number": "F018", "category": "Organic", "manufacturer": "LocalAg", "mfg_date": "2026-05-01", "exp_date": "2027-05-01", "brand": "PureOrg", "qr_code": "https://qr.io/f/F018"},
        {"id": 19, "product_name": "Potash Plus", "batch_number": "F019", "category": "Potassium", "manufacturer": "ICL", "mfg_date": "2025-11-15", "exp_date": "2027-11-15", "brand": "SoluPot", "qr_code": "https://qr.io/f/F019"},
        {"id": 20, "product_name": "Trace Element", "batch_number": "F020", "category": "Micronutrient", "manufacturer": "Valagro", "mfg_date": "2026-02-28", "exp_date": "2028-02-28", "brand": "MicroMix", "qr_code": "https://qr.io/f/F020"},
    ]
}

# --- 3. ENDPOINTS (NJIA ZA API) ---

@app.get("/")
def home():
    return {"message": "Welcome to the Agri-Input API. Use /docs to see the full documentation."}

@app.get("/api/v1/seeds")
def get_all_seeds(api_key: str = Security(validate_api_key)):
    return {"status": "success", "total": len(data_store["seeds"]), "items": data_store["seeds"]}

@app.get("/api/v1/fertilizers")
def get_all_fertilizers(api_key: str = Security(validate_api_key)):
    return {"status": "success", "total": len(data_store["fertilizers"]), "items": data_store["fertilizers"]}

@app.get("/api/v1/search")
def search_by_name(product_name: str, api_key: str = Security(validate_api_key)):
    results = []
    # Search in both seeds and fertilizers
    for category in data_store:
        for item in data_store[category]:
            if product_name.lower() in item["product_name"].lower():
                results.append(item)
    
    if not results:
        return {"status": "not found", "message": f"No product found with name: {product_name}"}
    
    return {"status": "success", "results": results}

if __name__ == "__main__":
    import uvicorn
    # Use port 8000 for local testing
    uvicorn.run(app, host="0.0.0.0", port=8000)
