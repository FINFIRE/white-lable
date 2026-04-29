"""
Capital type document registry for the Matching Algorithm.

Maps each capital type name to its [definition, faq, twelve-variable] report
functions from the capitalinformation subpackage.
"""
from .capitalinformation import (
    ownerdebtcashsaving1, acceleratoruniversity2, incubatoruniversity3,
    acceleratorpublic4, incubatorpublic5, smallbusinessadministrationsbasbaveteran6,
    royaltyfinancingtoplinerevenue7, grantsmunicipalities8,
    ownerdebtwholelifeinsurance9, privateequitysecuritiessafesimpleagreementfutureequity10,
    grantsgovernment11, ownerdebthomeequity12,
    smallbusinessadministrationsbasbaexpress13, acceleratorprivate14,
    commercialbankingequipmentloan15, commercialbankingsblc16,
    grantseducation17, grantsstateagencies18, incubatorprivate19,
    smallbusinessadministrationsbasbic20, commercialbankinglineofcredit21,
    commercialbankingrealestate22, governmentincentivesopportunityzone23,
    ownerdebtretirement401ksdi24, privateequitysecuritiesfamilyfriends25,
    smallbusinessadministrationsbasba504b26, smallbusinessadministrationsbasba7a27,
    commercialbankingcommercialbankloann28, governmentincentivesenterprisezones29,
    commercialbankingacquisitionloan30, grantsresearch31,
    ownerdebtpersonalcreditcards32, smallbusinessadministrationsbacdcsbdc33,
    commercialbankingassetbasedlending34, ownerdebtpersonalresourcesorloans35,
    privatedebtpromissorynote36, commercialbankingcollateralizeddebt37,
    privatedebtrealestateloan38, privateequitysecuritiesfamilyoffices39,
    privatedebtassetbasedlending40, privatedebtbridgefinancing41,
    privatedebtprivatedebt42, alternativeapps43,
    commercialbankingcreditcard44, digitalcurrencycryptowallet45,
    privateequitysecuritiesangelinvestors46, privateequitysecuritiesconvertiblenote47,
    grantscorporate48, privatedebtacquisitionloan49,
    privatedebthardmoneyloan50, alternativecorporatecredit51,
    factoringaccountsreceivable52, factoringmerchantaccount53,
    bondsgovernmentbacked54, bondshighyieldjunk55,
    bondsmortgagebacked56, factoringpurchaseorder57,
    privatedebtcollateralizeddebt58, factoringinvoice59,
    governmentincentivesgoldstar60, hedgefundspublic61,
    investmentbankingmezzaninefinancing62, privateequitysecuritiesregulationd506b63,
    digitalcurrencystablecoins64, bondsforeign65,
    privateequitysecuritiesregulationd506c66, privateequitysecuritiesrule14467,
    alternativehighyield68, investmentbankinginvestmentbankerdebt69,
    privateequitysecuritiesregulationd50570, privateequitysecuritiessophisticatedindividuals71,
    bondsinvestmentgrade72, hedgefundsprivate73,
    privateequitysecuritiesregulationd50474, digitalcurrencycryptocurrency75,
    governmentincentiveseb576, investmentbankingbrokersyndication77,
    privateequitysecuritiesaccreditedinvestors78, venturecapitalshorttermbridgefinancing79,
    digitalcurrencytokenization80, privateequitysecuritiesprivateplacementmemorandum81,
    privateequitysecuritiesregulationa82, privateequitysecuritiesregulationaplus83,
    privateequitysecuritiesregulationcftittleiii84, digitalcurrencyico85,
    digitalcurrencyieo86, investmentbankingbrokerdealerrepresentation87,
    investmentbankingequitysale88, privateequitysecuritiesbrokerdealers89,
    publicsecuritiesderivatives90, publicsecuritiesspacspecialpurposeacquisitioncompany91,
    venturecapitalmezzaninefinancing92, publicsecuritiesmarketmaker93,
    publicsecuritiesmoneymarketinstruments94,
    publicsecuritiespipeprivateinvestmentinpublicentity95,
    venturecapitallongtermdebt96, publicsecuritiesinitialpublicofferingipo97,
    publicsecuritiesotcoverthecounter98, venturecapitalmergersacquisitionsfinancing99,
    venturecapitalequitysale100,
)


def _entry(mod, base, faq_suffix='faq', twelve_suffix='twelve'):
    """
    Build a [definition_func, faq_func, twelve_func] list for a capital module.

    Args:
        mod: The imported module.
        base: Base function name (e.g. 'ownerdebtcashsaving').
        faq_suffix: Suffix appended to base for the FAQ function.
        twelve_suffix: Suffix appended to base for the twelve-variable function.
    """
    return [
        getattr(mod, base),
        getattr(mod, base + faq_suffix),
        getattr(mod, base + twelve_suffix),
    ]


# Registry: capital type display name -> [definition_fn, faq_fn, twelve_fn]
# Each function takes (request) and returns an HttpResponse.
CAPITAL_DOCUMENT_REGISTRY = {
    'Owner Debt - Cash Savings': _entry(ownerdebtcashsaving1, 'ownerdebtcashsaving', 'faq', 'twelve'),
    'Accelerator University': _entry(acceleratoruniversity2, 'acceleratoruniversity', 'faq', 'twelve'),
    'Incubator - University': _entry(incubatoruniversity3, 'incubatoruniversity', 'faq', 'twelve'),
    'Accelerator - Public': _entry(acceleratorpublic4, 'acceleratorpublic', 'faq', 'twelve'),
    'Incubator - Public': _entry(incubatorpublic5, 'incubatorpublic', 'faq', 'twelve'),
    'Small Business Administration (SBA) - SBA Veteran': _entry(smallbusinessadministrationsbasbaveteran6, 'smallbusinessadministrationsbasbaveteran', 'faq', 'twelve'),
    'Royalty Financing - Top Line Revenue': _entry(royaltyfinancingtoplinerevenue7, 'royaltyfinancingtoplinerevenue', 'faq', 'twelve'),
    'Grants - Municipalities': _entry(grantsmunicipalities8, 'grantsmunicipalities', 'faq', 'twelve'),
    'Owner Debt - Whole Life Insurance': _entry(ownerdebtwholelifeinsurance9, 'ownerdebtwholelifeinsurance', 'faq', 'twelve'),
    'Private Equity Securities - SAFE  Simple Agreement Future Equity': _entry(privateequitysecuritiessafesimpleagreementfutureequity10, 'privateequitysecuritiessafesimpleagreementfutureequity', 'faq', 'twelve'),
    'Grants - Government': _entry(grantsgovernment11, 'grantsgovernment', 'faq', 'twelve'),
    'Owner Debt - Home Equity': _entry(ownerdebthomeequity12, 'ownerdebthomeequity', 'faq', 'twelve'),
    'Small Business Administration (SBA) - SBA Express': _entry(smallbusinessadministrationsbasbaexpress13, 'smallbusinessadministrationsbasbaexpress', 'faq', 'twelve'),
    'Accelerator - Private': _entry(acceleratorprivate14, 'acceleratorprivate', 'faq', 'twelve'),
    'Commercial Banking - Equipment Loan': _entry(commercialbankingequipmentloan15, 'commercialbankingequipmentloan', 'faq', 'twelve'),
    'Commercial Banking - Standby Letter of Credit (SBLC)': _entry(commercialbankingsblc16, 'commercialbankingsblc', 'faq', 'twelve'),
    'Grants - Education Grants': _entry(grantseducation17, 'grantseducation', 'faq', 'twelve'),
    'Grants - State Agencies': _entry(grantsstateagencies18, 'grantsstateagencies', 'faq', 'twelve'),
    'Incubator - Private': _entry(incubatorprivate19, 'incubatorprivate', 'faq', 'twelve'),
    'Small Business Administration (SBA) - SBIC': _entry(smallbusinessadministrationsbasbic20, 'smallbusinessadministrationsbasbic', 'faq', 'twelve'),
    'Commercial Banking - Line of Credit': _entry(commercialbankinglineofcredit21, 'commercialbankinglineofcredit', 'faq', 'twelve'),
    'Commercial Banking - Real Estate Loan': _entry(commercialbankingrealestate22, 'commercialbankingrealestate', 'faq', 'twelve'),
    'Government Incentives Opportunity Zone Tax Credit Fund': _entry(governmentincentivesopportunityzone23, 'governmentincentivesopportunityzone', 'faq', 'twelve'),
    'Owner Debt - Retirement (401K) SDI': _entry(ownerdebtretirement401ksdi24, 'ownerdebtretirement401ksdi', 'faq', 'twelve'),
    'Private Equity Securities - Family and Friends': _entry(privateequitysecuritiesfamilyfriends25, 'privateequitysecuritiesfamilyfriends', 'faq', 'twelve'),
    'Small Business Administration (SBA) - SBA 504B': _entry(smallbusinessadministrationsbasba504b26, 'smallbusinessadministrationsbasba504b', 'faq', 'twelve'),
    'Small Business Administration (SBA) - SBA 7A': _entry(smallbusinessadministrationsbasba7a27, 'smallbusinessadministrationsbasba7a', 'faq', 'twelve'),
    'Commercial Banking - Commercial Bank Loan': _entry(commercialbankingcommercialbankloann28, 'commercialbankingcommercialbankloann', 'faq', 'twelve'),
    'Government Incentives - Enterprise Zones': _entry(governmentincentivesenterprisezones29, 'governmentincentivesenterprisezones', 'faq', 'twelve'),
    'Commercial Banking - Acquisition Loan': _entry(commercialbankingacquisitionloan30, 'commercialbankingacquisitionloan', 'faq', 'twelve'),
    'Grants - Research Grants': _entry(grantsresearch31, 'grantsresearch', 'faq', 'twelve'),
    'Owner Debt - Personal Credit Cards': _entry(ownerdebtpersonalcreditcards32, 'ownerdebtpersonalcreditcards', 'faq', 'twelve'),
    'Small Business Administration (SBA) - CDC/SBDC': _entry(smallbusinessadministrationsbacdcsbdc33, 'smallbusinessadministrationsbacdcsbdc', 'faq', 'twelve'),
    'Commercial Banking - Asset Based Lending': _entry(commercialbankingassetbasedlending34, 'commercialbankingassetbasedlending', 'faq', 'twelve'),
    'Owner Debt - Personal Resources or Loans': _entry(ownerdebtpersonalresourcesorloans35, 'ownerdebtpersonalresourcesorloans', 'faq', 'twelve'),
    'Private Debt - Promissory Note': _entry(privatedebtpromissorynote36, 'privatedebtpromissorynote', 'faq', 'twelve'),
    'Commercial Banking - Collateralized Debt': _entry(commercialbankingcollateralizeddebt37, 'commercialbankingcollateralizeddebt', 'faq', 'twelve'),
    'Private Debt - Real Estate Loan': _entry(privatedebtrealestateloan38, 'privatedebtrealestateloan', 'faq', 'twelve'),
    'Private Equity Securities - Family Offices': _entry(privateequitysecuritiesfamilyoffices39, 'privateequitysecuritiesfamilyoffices', 'faq', 'twelve'),
    'Private Debt - Asset Based Lending': _entry(privatedebtassetbasedlending40, 'privatedebtassetbasedlending', 'faq', 'twelve'),
    'Private Debt - Bridge Financing': _entry(privatedebtbridgefinancing41, 'privatedebtbridgefinancing', 'faq', 'twelve'),
    'Private Debt - Private Debt': _entry(privatedebtprivatedebt42, 'privatedebtprivatedebt', 'faq', 'twelve'),
    'Alternative - Apps (i.e. Cabbage)': _entry(alternativeapps43, 'alternativeapps', 'faq', 'twelve'),
    'Commercial Banking - Credit Card': _entry(commercialbankingcreditcard44, 'commercialbankingcreditcard', 'faq', 'twelve'),
    'Digital Currency - Investment via Crypto Wallet': [digitalcurrencycryptowallet45.digitalcurrencycryptowallet, digitalcurrencycryptowallet45.digitalcurrencycryptofaq, digitalcurrencycryptowallet45.digitalcurrencycryptowallettwelve],
    'Private Equity Securities - Angel Investors': _entry(privateequitysecuritiesangelinvestors46, 'privateequitysecuritiesangelinvestors', 'faq', 'twelve'),
    'Private Equity Securities - Convertible Note': _entry(privateequitysecuritiesconvertiblenote47, 'privateequitysecuritiesconvertiblenote', 'faq', 'twelve'),
    'Grants - Corporate Grants': _entry(grantscorporate48, 'grantscorporate', 'faq', 'twelve'),
    'Private Debt - Acquisition Loan': _entry(privatedebtacquisitionloan49, 'privatedebtacquisitionloan', 'faq', 'twelve'),
    'Private Debt - Hard Money Loan': _entry(privatedebthardmoneyloan50, 'privatedebthardmoneyloan', 'faq', 'twelve'),
    'Alternative - Corporate Credit (Third Party)': _entry(alternativecorporatecredit51, 'alternativecorporatecredit', 'faq', 'twelve'),
    'Factoring - Accounts Receivable Loans': _entry(factoringaccountsreceivable52, 'factoringaccountsreceivable', 'faq', 'twelve'),
    'Factoring - Merchant Account Advances': _entry(factoringmerchantaccount53, 'factoringmerchantaccount', 'faq', 'twelve'),
    'Bonds - Government Backed': _entry(bondsgovernmentbacked54, 'bondsgovernmentbacked', 'faq', 'twelve'),
    'Bonds - High Yield Junk': _entry(bondshighyieldjunk55, 'bondshighyieldjunk', 'faq', 'twelve'),
    'Bonds - Mortgage Backed': _entry(bondsmortgagebacked56, 'bondsmortgagebacked', 'faq', 'twelve'),
    'Factoring - Purchase Order Loan': _entry(factoringpurchaseorder57, 'factoringpurchaseorder', 'faq', 'twelve'),
    'Private Debt - Collateralized Debt': _entry(privatedebtcollateralizeddebt58, 'privatedebtcollateralizeddebt', 'faq', 'twelve'),
    'Factoring - Invoice Factoring': _entry(factoringinvoice59, 'factoringinvoice', 'faq', 'twelve'),
    'Government Incentives - Gold Star': _entry(governmentincentivesgoldstar60, 'governmentincentivesgoldstar', 'faq', 'twelve'),
    'Hedge Funds - Public': _entry(hedgefundspublic61, 'hedgefundspublic', 'faq', 'twelve'),
    'Investment Banking - Mezzanine Financing': _entry(investmentbankingmezzaninefinancing62, 'investmentbankingmezzaninefinancing', 'faq', 'twelve'),
    'Private Equity Securities - Regulation D 506(b)': _entry(privateequitysecuritiesregulationd506b63, 'privateequitysecuritiesregulationd506b', 'faq', 'twelve'),
    'Digital Currency - Stable Coins (DAO) - Blockchain': _entry(digitalcurrencystablecoins64, 'digitalcurrencystablecoins', 'faq', 'twelve'),
    'Bonds - Foreign': _entry(bondsforeign65, 'bondsforeign', 'faq', 'twelve'),
    'Private Equity Securities - Regulation D 506(c)': _entry(privateequitysecuritiesregulationd506c66, 'privateequitysecuritiesregulationd506c', 'faq', 'twelve'),
    'Private Equity Securities - Rule 144': [privateequitysecuritiesrule14467.privateequitysecuritiesrule144, privateequitysecuritiesrule14467.privateequitysecuritiesrule144faq, privateequitysecuritiesrule14467.privateequitysecuritiesrule144twelve],
    'Alternative - High Yield Business Consumer Loan': _entry(alternativehighyield68, 'alternativehighyield', 'faq', 'twelve'),
    'Investment Banking - Investment Banker Debt': _entry(investmentbankinginvestmentbankerdebt69, 'investmentbankinginvestmentbankerdebt', 'faq', 'twelve'),
    'Private Equity Securities - Regulation D 505': [privateequitysecuritiesregulationd50570.privateequitysecuritiesregulationd505, privateequitysecuritiesregulationd50570.privateequitysecuritiesregulationd505faq, privateequitysecuritiesregulationd50570.privateequitysecuritiesregulationd505twelve],
    'Private Equity Securities - Sophisticated Individuals': [privateequitysecuritiessophisticatedindividuals71.privateequitysecuritiessophisticatedindividuals, privateequitysecuritiessophisticatedindividuals71.privateequitysecuritiessophisticatedindividualsfaq, privateequitysecuritiessophisticatedindividuals71.privateequitysecuritiessophisticatedindividualstwelve],
    'Bonds - Investment Grade': _entry(bondsinvestmentgrade72, 'bondsinvestmentgrade', 'faq', 'twelve'),
    'Hedge Funds - Private': _entry(hedgefundsprivate73, 'hedgefundsprivate', 'faq', 'twelve'),
    'Private Equity Securities - Regulation D 504': [privateequitysecuritiesregulationd50474.privateequitysecuritiesregulationd504, privateequitysecuritiesregulationd50474.privateequitysecuritiesregulationd504faq, privateequitysecuritiesregulationd50474.privateequitysecuritiesregulationd504twelve],
    'Digital Currency - Cryptocurrency': _entry(digitalcurrencycryptocurrency75, 'digitalcurrencycryptocurrency', 'faq', 'twelve'),
    'Government Incentives - EB5 Immigration': [governmentincentiveseb576.governmentincentiveseb5, governmentincentiveseb576.governmentincentiveseb5faq, governmentincentiveseb576.governmentincentiveseb5twelve],
    'Investment Banking - Broker Syndication': _entry(investmentbankingbrokersyndication77, 'investmentbankingbrokersyndication', 'faq', 'twelve'),
    'Private Equity Securities - Accredited Investors': _entry(privateequitysecuritiesaccreditedinvestors78, 'privateequitysecuritiesaccreditedinvestors', 'faq', 'twelve'),
    'Venture Capital - Short-Term Bridge Financing': _entry(venturecapitalshorttermbridgefinancing79, 'venturecapitalshorttermbridgefinancing', 'faq', 'twelve'),
    'Digital Currency - Tokenization': _entry(digitalcurrencytokenization80, 'digitalcurrencytokenization', 'faq', 'twelve'),
    'Private Equity Securities - Private Placement Memorandum': _entry(privateequitysecuritiesprivateplacementmemorandum81, 'privateequitysecuritiesprivateplacementmemorandum', 'faq', 'twelve'),
    'Private Equity Securities - Regulation A': _entry(privateequitysecuritiesregulationa82, 'privateequitysecuritiesregulationa', 'faq', 'twelve'),
    'Private Equity Securities - Regulation A Plus': _entry(privateequitysecuritiesregulationaplus83, 'privateequitysecuritiesregulationaplus', 'faq', 'twelve'),
    'Private Equity Securities - Regulation CF Tittle III': _entry(privateequitysecuritiesregulationcftittleiii84, 'privateequitysecuritiesregulationcftittleiii', 'faq', 'twelve'),
    'Digital Currency - Initial Coin Offering': _entry(digitalcurrencyico85, 'digitalcurrencyico', 'faq', 'twelve'),
    'Digital Currency - Initial Exchange Offering': _entry(digitalcurrencyieo86, 'digitalcurrencyieo', 'faq', 'twelve'),
    'Investment Banking - Broker Dealer Representation': _entry(investmentbankingbrokerdealerrepresentation87, 'investmentbankingbrokerdealerrepresentation', 'faq', 'twelve'),
    'Investment Banking - Equity Sale': _entry(investmentbankingequitysale88, 'investmentbankingequitysale', 'faq', 'twelve'),
    'Private Equity Securities - Broker Dealers': _entry(privateequitysecuritiesbrokerdealers89, 'privateequitysecuritiesbrokerdealers', 'faq', 'twelve'),
    'Public Securities - Derivatives': [publicsecuritiesderivatives90.publicsecuritiesderivatives, publicsecuritiesderivatives90.publicsecuritiesderivativesfaq, publicsecuritiesderivatives90.publicsecuritiesderivativestwelve],
    'Public Securities - SPAC - Special Purpose Acquisition Company': [publicsecuritiesspacspecialpurposeacquisitioncompany91.publicsecuritiesspacspecialpurposeacquisitioncompany, publicsecuritiesspacspecialpurposeacquisitioncompany91.publicsecuritiesspacspecialpurposeacquisitioncompanyfaq, publicsecuritiesspacspecialpurposeacquisitioncompany91.publicsecuritiesspacspecialpurposeacquisitioncompanytwelve],
    'Venture Capital - Mezzanine Financing': _entry(venturecapitalmezzaninefinancing92, 'venturecapitalmezzaninefinancing', 'faq', 'twelve'),
    'Public Securities - Market Maker': _entry(publicsecuritiesmarketmaker93, 'publicsecuritiesmarketmaker', 'faq', 'twelve'),
    'Public Securities - Money Market Instruments': _entry(publicsecuritiesmoneymarketinstruments94, 'publicsecuritiesmoneymarketinstruments', 'faq', 'twelve'),
    'Public Securities - PIPE Private Investment in Public Entity': [publicsecuritiespipeprivateinvestmentinpublicentity95.publicsecuritiespipeprivateinvestmentinpublicentity, publicsecuritiespipeprivateinvestmentinpublicentity95.publicsecuritiespipeprivateinvestmentinpublicentityfaq, publicsecuritiespipeprivateinvestmentinpublicentity95.publicsecuritiespipeprivateinvestmentinpublicentitytwelve],
    'Venture Capital - Long Term Debt': _entry(venturecapitallongtermdebt96, 'venturecapitallongtermdebt', 'faq', 'twelve'),
    'Public Securities - Initial Public Offering (IPO)': [publicsecuritiesinitialpublicofferingipo97.publicsecuritiesinitialpublicofferingipo, publicsecuritiesinitialpublicofferingipo97.publicsecuritiesinitialpublicofferingipofaq, publicsecuritiesinitialpublicofferingipo97.publicsecuritiesinitialpublicofferingipotwelve],
    'Public Securities - OTC Over the Counter': _entry(publicsecuritiesotcoverthecounter98, 'publicsecuritiesotcoverthecounter', 'faq', 'twelve'),
    'Venture Capital - Mergers and Acquisitions Financing': _entry(venturecapitalmergersacquisitionsfinancing99, 'venturecapitalmergersacquisitionsfinancing', 'faq', 'twelve'),
    'Venture Capital - Equity Sale': _entry(venturecapitalequitysale100, 'venturecapitalequitysale', 'faq', 'twelve'),
}


def get_capital_documents(capital_name, request):
    """
    Get the [definition, faq, twelve-variable] HttpResponse objects for a capital type.

    Args:
        capital_name: Display name of the capital type.
        request: Django HttpRequest object.

    Returns:
        List of 3 HttpResponse objects: [definition, faq, twelve_variable].
    """
    funcs = CAPITAL_DOCUMENT_REGISTRY[capital_name]
    return [fn(request) for fn in funcs]
