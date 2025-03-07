# **Blue Cross Blue Shield Web Scraper - Endocrinologists Data Extraction**

## **📌 Project Overview**
This Python script automates the process of retrieving **Endocrinologists' details** from the **Blue Cross Blue Shield (BCBS) API**. It:
1. **Searches for providers** using the **Search API**.
2. **Fetches additional details** (education, affiliations, other locations) using the **Profile API**.
3. **Saves the extracted data** into structured **CSV files**.

## **📂 File Structure**
```
/WebScraper
│── webcrawler.py        # Main script for data extraction
│── combine_csv.py       # Script to merge multiple CSV files
│── README.md            # Project documentation (this file)
│── output/
│   ├── endocrinologists_page_1.csv
│   ├── endocrinologists_page_2.csv
│   ├── ...
│   ├── merged_endocrinologists.csv
```

---

## **🔧 Requirements**
### **1️⃣ Install Dependencies**
Ensure you have Python **3.7+** installed. Then, install required libraries:
```sh
pip install requests pandas
```

---

## **🚀 Usage Instructions**
### **Step 1: Run the Web Scraper**
The script fetches **one page at a time** (each containing **20 providers**) to avoid API rate limits. Update the **page number manually** before running it again.
```sh
python webcrawler.py
```
- **Data is saved as `endocrinologists_page_<page>.csv`** in the output folder.

---

### **Step 2: Merge All CSV Files**
Once all pages have been extracted, use `combine_csv.py` to **merge them into one final dataset**.
```sh
python combine_csv.py
```
- **Final file:** `merged_endocrinologists.csv`

---

## **🛠 How the Script Works**
### **🔍 Step 1: Search API Request**
- Sends a **GET request** to `https://digitalapi.bluecrossma.com/digital/find-a-doctor/v2/providers`
- Filters results based on **Endocrinology specialty, location, and telehealth availability**.
- Extracts **Basic details**: 
  - `Name`, `Specialty`, `Gender`, `Primary Location`, `Phone`, `Distance`
  
### **📄 Step 2: Profile API Request**
- Uses `providerId` and `locationId` from the Search API.
- Retrieves **additional details**:
  - **Education**: Medical school & graduation year.
  - **Affiliated Hospitals**: Where the doctor practices.
  - **Group Affiliations**: Associated medical groups.
  - **Other Locations**: Additional practice locations.

### **📊 Step 3: Data Storage**
- Each page of **20 providers** is saved as `endocrinologists_page_<page>.csv`.
- The **final merged dataset** includes all collected pages.

---

## **📌 Key Features**
✅ **Handles pagination manually** – one page per run to avoid expired tokens.  
✅ **Fetches both primary and additional locations** for doctors.  
✅ **Extracts education and hospital affiliations** for better insights.  
✅ **Saves results in structured CSV format** for easy analysis.  

---

## **⚠️ API Token Expiry Handling**
The API token **expires frequently**, so **you must update it manually** in the script before each run:
```python
"Authorization": "Bearer YOUR_NEW_ACCESS_TOKEN"
```
> **Check the DevTools network tab in your browser** to get the latest `Authorization` token.

---

## **👨‍💻 Example Data Extracted**
| Name | Specialty | Gender | Primary Location | Education | Affiliated Hospitals | Other Locations |
|------|----------|--------|------------------|-----------|----------------------|----------------|
| Dr. John Doe | Endocrinology | M | Brigham Hospital, MA | Harvard Medical School | Massachusetts General Hospital | Boston Medical Center |

---

## **❓ Troubleshooting**
### **1️⃣ API Returns `401 Unauthorized`**
- The token has expired. **Update the `Authorization` header**.
- Refresh the token using BCBS’s authentication flow.

### **2️⃣ `PermissionError: [Errno 13]` When Saving CSV**
- Close any open CSV files before running the script again.

### **3️⃣ `pandas.errors.EmptyDataError` in `combine_csv.py`**
- One or more CSV files are empty. Check and remove them before merging.

---

## **📜 License**
This project is for **educational purposes only**. Data fetched is subject to **BCBS terms and conditions**.

---

## **👨‍💻 Author**
**Jahnavi Mishra**  
🔗 **LinkedIn:** [Your Profile]  
📧 **Email:** [Your Email]  

---

**🎥 Next Steps:**  
- Record a **video demo** showing how the script works step by step! 🎬🚀
