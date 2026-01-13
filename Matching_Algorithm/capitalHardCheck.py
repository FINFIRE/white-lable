import copy
def capitalCheck(valueList=[], matchPercentageDictionary={}):
    a = copy.deepcopy(matchPercentageDictionary)
    if valueList[0] == 1:
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(c)'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(b)'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
        matchPercentageDictionary['Bonds - Mortgage Backed'] = 0
        matchPercentageDictionary['Commercial Banking - Acquisition Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Asset Based Lending'] = 0
        matchPercentageDictionary['Commercial Banking - Collateralized Debt'] = 0
        matchPercentageDictionary['Commercial Banking - Commercial Bank Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Equipment Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Line of Credit'] = 0
        matchPercentageDictionary['Commercial Banking - Real Estate Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Standby Letter of Credit (SBLC)'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0 
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0

    if valueList[1] == 1:
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
        matchPercentageDictionary['Bonds - Mortgage Backed'] = 0
        matchPercentageDictionary['Commercial Banking - Acquisition Loan'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        
    if valueList[2] == 1:
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
        matchPercentageDictionary['Bonds - Mortgage Backed'] = 0
        matchPercentageDictionary['Commercial Banking - Acquisition Loan'] = 0
    if valueList[3] == 1:
        matchPercentageDictionary['Incubator - University'] = 0
    if valueList[4] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0 
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
    if valueList[5] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Grants - Government'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[6] == 1:
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
        matchPercentageDictionary['Commercial Banking - Acquisition Loan'] = 0 
        matchPercentageDictionary['Commercial Banking - Asset Based Lending'] = 0
        matchPercentageDictionary['Commercial Banking - Collateralized Debt'] = 0
        matchPercentageDictionary['Commercial Banking - Equipment Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Real Estate Loan'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[7] == 1:
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(c)'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(b)'] = 0
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Grants - Government'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
        matchPercentageDictionary['Bonds - Mortgage Backed'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
        matchPercentageDictionary['Commercial Banking - Acquisition Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Asset Based Lending'] = 0
        matchPercentageDictionary['Commercial Banking - Collateralized Debt'] = 0
        matchPercentageDictionary['Commercial Banking - Commercial Bank Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Equipment Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Real Estate Loan'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[8] == 1:
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(c)'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(b)'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
        matchPercentageDictionary['Bonds - Mortgage Backed'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[9] == 1:
        pass
    if valueList[10] == 1:
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
    if valueList[11] == 1:
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
    if valueList[12] == 1:
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
    if valueList[13] == 1:
        pass
    if valueList[14] == 1:
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
        matchPercentageDictionary['Bonds - Mortgage Backed'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
        matchPercentageDictionary['Commercial Banking - Acquisition Loan'] = 0
    if valueList[15] == 1:
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
        matchPercentageDictionary['Bonds - Mortgage Backed'] = 0
        matchPercentageDictionary['Commercial Banking - Acquisition Loan'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[16] == 1:
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
    if valueList[17] == 1:
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
    if valueList[18] == 1:
        matchPercentageDictionary['Incubator - University'] = 0
    if valueList[19] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
    if valueList[20] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
    if valueList[21] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
    if valueList[22] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(b)'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[23] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(b)'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[24] == 1:
        pass
    if valueList[25] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[26] == 1:
        pass
    if valueList[27] == 1:
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[28] == 1:
        pass
    if valueList[29] == 1:
        pass
    if valueList[30] == 1:
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[31] == 1:
        pass
    if valueList[32] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
    if valueList[33] == 1:
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
    if valueList[34] == 1:
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[35] == 1:
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
    if valueList[36] == 1:
         pass
    if valueList[37] == 1:
        pass
    if valueList[38] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[39] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        
    if valueList[40] == 1:
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[41] == 1:
        pass
    if valueList[42] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
    if valueList[43] == 1:
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
    if valueList[44] == 1:
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
        matchPercentageDictionary['Bonds - Mortgage Backed'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
        matchPercentageDictionary['Commercial Banking - Acquisition Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Collateralized Debt'] = 0
        matchPercentageDictionary['Commercial Banking - Real Estate Loan'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[45] == 1:
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
        matchPercentageDictionary['Bonds - Mortgage Backed'] = 0
        matchPercentageDictionary['Commercial Banking - Acquisition Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Collateralized Debt'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[46] == 1:
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
        matchPercentageDictionary['Commercial Banking - Collateralized Debt'] = 0
    if valueList[47] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
    if valueList[48] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Grants - Government'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
    if valueList[49] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Grants - Government'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
    if valueList[50] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Grants - Government'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Commercial Banking - Line of Credit'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
    if valueList[51] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Grants - Government'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Commercial Banking - Line of Credit'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
    if valueList[52] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(b)'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Grants - Government'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Commercial Banking - Equipment Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Line of Credit'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
    if valueList[53] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(b)'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Grants - Government'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Commercial Banking - Equipment Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Line of Credit'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
    if valueList[54] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(b)'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Grants - Government'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Commercial Banking - Equipment Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Line of Credit'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[55] == 1:
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        
    if valueList[56] == 1:
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(c)'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(b)'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
        matchPercentageDictionary['Bonds - Mortgage Backed'] = 0
        matchPercentageDictionary['Commercial Banking - Acquisition Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Asset Based Lending'] = 0
        matchPercentageDictionary['Commercial Banking - Collateralized Debt'] = 0
        matchPercentageDictionary['Commercial Banking - Equipment Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Real Estate Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Standby Letter of Credit (SBLC)'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
    if valueList[57] == 1:
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
        matchPercentageDictionary['Bonds - Mortgage Backed'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
    if valueList[58] == 1:
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
        matchPercentageDictionary['Bonds - Mortgage Backed'] = 0
    if valueList[59] == 1:
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
    if valueList[60] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[61] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[62] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Grants - Government'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[63] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Grants - Government'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        matchPercentageDictionary['Commercial Banking - Commercial Bank Loan'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[64] == 1:
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
    if valueList[65] == 1:
        pass
    if valueList[66] == 1:
        pass
    if valueList[67] == 1:
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
    if valueList[68] == 1:
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Bonds - Government Backed'] = 0
        matchPercentageDictionary['Bonds - High Yield Junk'] = 0
        matchPercentageDictionary['Bonds - Investment Grade'] = 0
        matchPercentageDictionary['Bonds - Mortgage Backed'] = 0
        matchPercentageDictionary['Commercial Banking - Asset Based Lending'] = 0
        matchPercentageDictionary['Commercial Banking - Collateralized Debt'] = 0
        matchPercentageDictionary['Commercial Banking - Equipment Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Line of Credit'] = 0
        matchPercentageDictionary['Commercial Banking - Real Estate Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Standby Letter of Credit (SBLC)'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        
    if valueList[69] == 1:
        matchPercentageDictionary['Grants - Education Grants'] = 0
    if valueList[70] == 1:
        matchPercentageDictionary['Grants - Education Grants'] = 0
    if valueList[71] == 1:
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[72] == 1:
        pass
    if valueList[73] == 1:
        pass
    if valueList[74] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Grants - Government'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[75] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
    if valueList[76] == 1:
        matchPercentageDictionary['Grants - Government'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
    if valueList[77] == 1:
        pass
    if valueList[78] == 1:
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
        matchPercentageDictionary['Commercial Banking - Asset Based Lending'] = 0
        matchPercentageDictionary['Commercial Banking - Collateralized Debt'] = 0
        matchPercentageDictionary['Commercial Banking - Equipment Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Real Estate Loan'] = 0
    if valueList[79] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(c)'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(b)'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Accelerator - Private'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Commercial Banking - Acquisition Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Commercial Bank Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[80] == 1:
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
    if valueList[81] == 1:
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
    if valueList[82] == 1:
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(c)'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(b)'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Bonds - Foreign'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Commercial Banking - Acquisition Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Asset Based Lending'] = 0
        matchPercentageDictionary['Commercial Banking - Collateralized Debt'] = 0
        matchPercentageDictionary['Commercial Banking - Commercial Bank Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
        matchPercentageDictionary['Commercial Banking - Equipment Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Real Estate Loan'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[83] == 1:
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
    if valueList[84] == 1:
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
    if valueList[85] == 1:
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
    if valueList[86] == 1:
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Owner Debt - Whole Life Insurance'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
    if valueList[87] == 1:
        pass
    if valueList[88] == 1:
        pass
    if valueList[89] == 1:
        pass
    if valueList[90] == 1:
        pass
    if valueList[91] == 1:
        pass
    if valueList[92] == 1:
        pass
    if valueList[93] == 1:
        pass
    if valueList[94] == 1:
        pass
    if valueList[95] == 1:
        pass
    if valueList[96] == 1:
        pass
    if valueList[97] == 1:
        pass
    if valueList[98] == 1:
        pass
    if valueList[99] == 1:
        pass
    if valueList[100] == 1:
        pass
    if valueList[101] == 1:
        pass
    if valueList[102] == 1:
        pass
    if valueList[103] == 1:
        pass
    if valueList[104] == 1:
        pass
    if valueList[105] == 1:
        pass
    if valueList[106] == 1:
        pass
    if valueList[107] == 1:
        pass
    if valueList[108] == 1:
        pass
    if valueList[109] == 1:
        pass
    if valueList[110] == 1:
        pass
    if valueList[111] == 1:
        pass
    if valueList[112] == 1:
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Commercial Banking - Asset Based Lending'] = 0
        matchPercentageDictionary['Commercial Banking - Collateralized Debt'] = 0
        matchPercentageDictionary['Commercial Banking - Equipment Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Real Estate Loan'] = 0
        
    if valueList[113] == 1:
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
        matchPercentageDictionary['Commercial Banking - Credit Card'] = 0
    if valueList[114] == 1:
        matchPercentageDictionary['Owner Debt - Home Equity'] = 0
        matchPercentageDictionary['Commercial Banking - Asset Based Lending'] = 0
        matchPercentageDictionary['Commercial Banking - Collateralized Debt'] = 0
        matchPercentageDictionary['Commercial Banking - Equipment Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Real Estate Loan'] = 0
    if valueList[115] == 1:
        matchPercentageDictionary['Commercial Banking - Asset Based Lending'] = 0
        matchPercentageDictionary['Commercial Banking - Collateralized Debt'] = 0
        matchPercentageDictionary['Commercial Banking - Equipment Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Real Estate Loan'] = 0
    if valueList[116] == 1:
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Owner Debt - Personal Credit Cards'] = 0
    if valueList[117] == 1:
        pass
    if valueList[118] == 1:
        pass
    if valueList[119] == 1:
        pass
    if valueList[120] == 1:
        pass
    if valueList[121] == 1:
        pass
    if valueList[122] == 1:
        pass
    if valueList[123] == 1:
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(c)'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(b)'] = 0
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Grants - Government'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
        matchPercentageDictionary['Commercial Banking - Commercial Bank Loan'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[124] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(c)'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(b)'] = 0
        matchPercentageDictionary['Private Debt - Hard Money Loan'] = 0
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
        matchPercentageDictionary['Commercial Banking - Acquisition Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Asset Based Lending'] = 0
        matchPercentageDictionary['Commercial Banking - Collateralized Debt'] = 0
        matchPercentageDictionary['Commercial Banking - Commercial Bank Loan'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    if valueList[125] == 1:
        matchPercentageDictionary['Incubator - Public'] = 0
        matchPercentageDictionary['Incubator - Private'] = 0
        matchPercentageDictionary['Incubator - University'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(c)'] = 0
        matchPercentageDictionary['Private Equity Securities - Regulation D 506(b)'] = 0
        matchPercentageDictionary['Owner Debt - Retirement (401K) SDI'] = 0
        matchPercentageDictionary['Accelerator - Public'] = 0
        matchPercentageDictionary['Accelerator University'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 504B'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA 7A'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Express'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBA Veteran'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - CDC/SBDC'] = 0
        matchPercentageDictionary['Small Business Administration (SBA) - SBIC'] = 0
        matchPercentageDictionary['Alternative - Apps (i.e. Cabbage)'] = 0
        matchPercentageDictionary['Owner Debt - Cash Savings'] = 0
        matchPercentageDictionary['Commercial Banking - Acquisition Loan'] = 0
        matchPercentageDictionary['Commercial Banking - Asset Based Lending'] = 0
        matchPercentageDictionary['Commercial Banking - Collateralized Debt'] = 0
        matchPercentageDictionary['Commercial Banking - Commercial Bank Loan'] = 0
        matchPercentageDictionary['Royalty Financing - Top Line Revenue'] = 0
        matchPercentageDictionary['Grants - Municipalities'] = 0
        matchPercentageDictionary['Private Equity Securities - SAFE  Simple Agreement Future Equity'] = 0
        matchPercentageDictionary['Grants - Education Grants'] = 0
        matchPercentageDictionary['Grants - State Agencies'] = 0
        matchPercentageDictionary['Government Incentives Opportunity Zone Tax Credit Fund'] = 0
    return(matchPercentageDictionary)
    return (a)