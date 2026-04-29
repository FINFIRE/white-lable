from django.urls import path
from .views import Match,summary,definition,faq,twelvevariable,pdf,word
#from .capitalinformation.ownerdebtcashsaving1 import ownerdebtcashsaving,ownerdebtcashsavingfaq,ownerdebtcashsavingtwelve
#from .capitalinformation.acceleratoruniversity2 import acceleratoruniversity,acceleratoruniversityfaq,acceleratoruniversitytwelve
#from .capitalinformation.incubatoruniversity3 import incubatoruniversity,incubatoruniversityfaq,incubatoruniversitytwelve
#from .capitalinformation.acceleratorpublic4 import acceleratorpublic,acceleratorpublicfaq,acceleratorpublictwelve
#from .capitalinformation.incubatorpublic5 import incubatorpublic,incubatorpublicfaq,incubatorpublictwelve
#from .capitalinformation.smallbusinessadministrationsbasbaveteran6 import smallbusinessadministrationsbasbaveteran,smallbusinessadministrationsbasbaveteranfaq,smallbusinessadministrationsbasbaveterantwelve
#from .capitalinformation.royaltyfinancingtoplinerevenue7 import royaltyfinancingtoplinerevenue,royaltyfinancingtoplinerevenuefaq,royaltyfinancingtoplinerevenuetwelve
#from .capitalinformation.grantsmunicipalities8 import grantsmunicipalities,grantsmunicipalitiesfaq,grantsmunicipalitiestwelve
#from .capitalinformation.ownerdebtwholelifeinsurance9 import ownerdebtwholelifeinsurance,ownerdebtwholelifeinsurancefaq,ownerdebtwholelifeinsurancetwelve
#from .capitalinformation.privateequitysecuritiessafesimpleagreementfutureequity10 import privateequitysecuritiessafesimpleagreementfutureequity,privateequitysecuritiessafesimpleagreementfutureequityfaq,privateequitysecuritiessafesimpleagreementfutureequitytwelve
#from .capitalinformation.grantsgovernment11 import grantsgovernment,grantsgovernmentfaq,grantsgovernmenttwelve
#from .capitalinformation.ownerdebthomeequity12 import ownerdebthomeequity,ownerdebthomeequityfaq,ownerdebthomeequitytwelve
#from .capitalinformation.smallbusinessadministrationsbasbaexpress13 import smallbusinessadministrationsbasbaexpress,smallbusinessadministrationsbasbaexpressfaq,smallbusinessadministrationsbasbaexpresstwelve
#from .capitalinformation.acceleratorprivate14 import acceleratorprivate,acceleratorprivatefaq,acceleratorprivatetwelve
#from .capitalinformation.commercialbankingequipmentloan15 import commercialbankingequipmentloan,commercialbankingequipmentloanfaq,commercialbankingequipmentloantwelve
#from .capitalinformation.commercialbankingsblc16 import commercialbankingsblc,commercialbankingsblcfaq,commercialbankingsblctwelve
#from .capitalinformation.grantseducation17 import grantseducation,grantseducationfaq,grantseducationtwelve
#from .capitalinformation.grantsstateagencies18 import grantsstateagencies,grantsstateagenciesfaq,grantsstateagenciestwelve
#from .capitalinformation.incubatorprivate19 import incubatorprivate,incubatorprivatefaq,incubatorprivatetwelve
#from .capitalinformation.smallbusinessadministrationsbasbic20 import smallbusinessadministrationsbasbic,smallbusinessadministrationsbasbicfaq,smallbusinessadministrationsbasbictwelve
#from .capitalinformation.commercialbankinglineofcredit21 import commercialbankinglineofcredit,commercialbankinglineofcreditfaq,commercialbankinglineofcredittwelve
#from .capitalinformation.commercialbankingrealestate22 import commercialbankingrealestate,commercialbankingrealestatesatefaq,commercialbankingrealestatetwelve
#from .capitalinformation.governmentincentivesopportunityzone23 import governmentincentivesopportunityzone,governmentincentivesopportunityzonefaq,governmentincentivesopportunityzonetwelve
#from .capitalinformation.ownerdebtretirement401ksdi24 import ownerdebtretirement401ksdi,ownerdebtretirement401ksdifaq,ownerdebtretirement401ksditwelve
#from .capitalinformation.privateequitysecuritiesfamilyfriends25 import privateequitysecuritiesfamilyfriends,privateequitysecuritiesfamilyfriendsfaq,privateequitysecuritiesfamilyfriendstwelve
#from .capitalinformation.smallbusinessadministrationsbasba504b26 import smallbusinessadministrationsbasba504b,smallbusinessadministrationsbasba504bfaq,smallbusinessadministrationsbasba504btwelve
#from .capitalinformation.smallbusinessadministrationsbasba7a27 import smallbusinessadministrationsbasba7a,smallbusinessadministrationsbasba7afaq,smallbusinessadministrationsbasba7atwelve
#from .capitalinformation.commercialbankingcommercialbankloann28 import commercialbankingcommercialbankloann,commercialbankingcommercialbankloannfaq,commercialbankingcommercialbankloanntwelve
#from .capitalinformation.governmentincentivesenterprisezones29 import governmentincentivesenterprisezones,governmentincentivesenterprisezonesfaq,governmentincentivesenterprisezonestwelve
#from .capitalinformation.commercialbankingacquisitionloan30 import commercialbankingacquisitionloan,commercialbankingacquisitionloanfaq,commercialbankingacquisitionloantwelve
#from .capitalinformation.grantsresearch31 import grantsresearch,grantsresearchfaq,grantsresearchtwelve
#from .capitalinformation.ownerdebtpersonalcreditcards32 import ownerdebtpersonalcreditcards,ownerdebtpersonalcreditcardsfaq,ownerdebtpersonalcreditcardstwelve
#from .capitalinformation.smallbusinessadministrationsbacdcsbdc33 import smallbusinessadministrationsbacdcsbdc,smallbusinessadministrationsbacdcsbdcfaq,smallbusinessadministrationsbacdcsbdctwelve
#from .capitalinformation.commercialbankingassetbasedlending34 import commercialbankingassetbasedlending,commercialbankingassetbasedlendingfaq,commercialbankingassetbasedlendingtwelve
#from .capitalinformation.ownerdebtpersonalresourcesorloans35 import ownerdebtpersonalresourcesorloans,ownerdebtpersonalresourcesorloansfaq,ownerdebtpersonalresourcesorloanstwelve
#from .capitalinformation.privatedebtpromissorynote36 import privatedebtpromissorynote,privatedebtpromissorynotefaq,privatedebtpromissorynotetwelve
#from .capitalinformation.commercialbankingcollateralizeddebt37 import commercialbankingcollateralizeddebt,commercialbankingcollateralizeddebtfaq,commercialbankingcollateralizeddebttwelve
#from .capitalinformation.privatedebtrealestateloan38 import privatedebtrealestateloan,privatedebtrealestateloanfaq,privatedebtrealestateloantwelve
#from .capitalinformation.privateequitysecuritiesfamilyoffices39 import privateequitysecuritiesfamilyoffices,privateequitysecuritiesfamilyofficesfaq,privateequitysecuritiesfamilyofficestwelve
#from .capitalinformation.privatedebtassetbasedlending40 import privatedebtassetbasedlending,privatedebtassetbasedlendingfaq,privatedebtassetbasedlendingtwelve
#from .capitalinformation.privatedebtbridgefinancing41 import privatedebtbridgefinancing,privatedebtbridgefinancingfaq,privatedebtbridgefinancingtwelve
#from .capitalinformation.privatedebtprivatedebt42 import privatedebtprivatedebt,privatedebtprivatedebtfaq,privatedebtprivatedebttwelve
#from .capitalinformation.alternativeapps43 import alternativeapps,alternativeappsfaq,alternativeappstwelve
#from .capitalinformation.commercialbankingcreditcard44 import commercialbankingcreditcard,commercialbankingcreditcardfaq,commercialbankingcreditcardtwelve
#from .capitalinformation.digitalcurrencycryptowallet45 import digitalcurrencycryptowallet,digitalcurrencycryptowalletfaq,digitalcurrencycryptowallettwelve
#from .capitalinformation.privateequitysecuritiesangelinvestors46 import privateequitysecuritiesangelinvestors,privateequitysecuritiesangelinvestorsfaq,privateequitysecuritiesangelinvestorstwelve
#from .capitalinformation.privateequitysecuritiesconvertiblenote47 import privateequitysecuritiesconvertiblenote,privateequitysecuritiesconvertiblenotefaq,privateequitysecuritiesconvertiblenotetwelve
#from .capitalinformation.grantscorporate48 import grantscorporate,grantscorporatefaq,grantscorporatetwelve
#from .capitalinformation.privatedebtacquisitionloan49 import privatedebtacquisitionloan,privatedebtacquisitionloanfaq,privatedebtacquisitionloantwelve
#from .capitalinformation.privatedebthardmoneyloan50 import privatedebthardmoneyloan,privatedebthardmoneyloanfaq,privatedebthardmoneyloantwelve
#from .capitalinformation.alternativecorporatecredit51 import alternativecorporatecredit,alternativecorporatecreditfaq,alternativecorporatecredittwelve
#from .capitalinformation.factoringaccountsreceivable52 import factoringaccountsreceivable,factoringaccountsreceivablefaq,factoringaccountsreceivabletwelve
#from .capitalinformation.factoringmerchantaccount53 import factoringmerchantaccount,factoringmerchantaccountfaq,factoringmerchantaccounttwelve
#from .capitalinformation.bondsgovernmentbacked54 import bondsgovernmentbacked,bondsgovernmentbackedfaq,bondsgovernmentbackedtwelve
#from .capitalinformation.bondshighyieldjunk55 import bondshighyieldjunk,bondshighyieldjunkfaq,bondshighyieldjunktwelve
#from .capitalinformation.bondsmortgagebacked56 import bondsmortgagebacked,bondsmortgagebackedfaq,bondsmortgagebackedtwelve
#from .capitalinformation.factoringpurchaseorder57 import factoringpurchaseorder,factoringpurchaseorderfaq,factoringpurchaseordertwelve
#from .capitalinformation.privatedebtcollateralizeddebt58 import privatedebtcollateralizeddebt,privatedebtcollateralizeddebtfaq,privatedebtcollateralizeddebttwelve
#from .capitalinformation.factoringinvoice59 import factoringinvoice,factoringinvoicefaq,factoringinvoicetwelve
#from .capitalinformation.governmentincentivesgoldstar60 import governmentincentivesgoldstar,governmentincentivesgoldstarfaq,governmentincentivesgoldstartwelve
#from .capitalinformation.hedgefundspublic61 import hedgefundspublic,hedgefundspublicfaq,hedgefundspublictwelve
#from .capitalinformation.investmentbankingmezzaninefinancing62 import investmentbankingmezzaninefinancing,investmentbankingmezzaninefinancingfaq,investmentbankingmezzaninefinancingtwelve
#from .capitalinformation.privateequitysecuritiesregulationd506b63 import privateequitysecuritiesregulationd506b,privateequitysecuritiesregulationd506bfaq,privateequitysecuritiesregulationd506btwelve
#from .capitalinformation.digitalcurrencystablecoins64 import digitalcurrencystablecoins,digitalcurrencystablecoinsfaq,digitalcurrencystablecoinstwelve
#from .capitalinformation.bondsforeign65 import bondsforeign,bondsforeignfaq,bondsforeigntwelve
#from .capitalinformation.privateequitysecuritiesregulationd506c66 import privateequitysecuritiesregulationd506c,privateequitysecuritiesregulationd506cfaq,privateequitysecuritiesregulationd506ctwelve
#from .capitalinformation.privateequitysecuritiesrule14467 import privateequitysecuritiesrule144,privateequitysecuritiesrule144faq,privateequitysecuritiesrule144twelve
#from .capitalinformation.alternativehighyield68 import alternativehighyield,alternativehighyieldfaq,alternativehighyieldtwelve
#from .capitalinformation.investmentbankinginvestmentbankerdebt69 import investmentbankinginvestmentbankerdebt,investmentbankinginvestmentbankerdebtfaq,investmentbankinginvestmentbankerdebttwelve
#from .capitalinformation.privateequitysecuritiesregulationd50570 import privateequitysecuritiesregulationd505,privateequitysecuritiesregulationd505faq,privateequitysecuritiesregulationd505twelve
#from .capitalinformation.privateequitysecuritiessophisticatedindividuals71 import privateequitysecuritiessophisticatedindividuals,privateequitysecuritiessophisticatedindividualsfaq,privateequitysecuritiessophisticatedindividualstwelve
#from .capitalinformation.bondsinvestmentgrade72 import bondsinvestmentgrade,bondsinvestmentgradefaq,bondsinvestmentgradetwelve
#from .capitalinformation.hedgefundsprivate73 import hedgefundsprivate,hedgefundsprivatefaq,hedgefundsprivatetwelve
#from .capitalinformation.privateequitysecuritiesregulationd50474 import privateequitysecuritiesregulationd504,privateequitysecuritiesregulationd504faq,privateequitysecuritiesregulationd504twelve
#from .capitalinformation.digitalcurrencycryptocurrency75 import digitalcurrencycryptocurrency,digitalcurrencycryptocurrencyfaq,digitalcurrencycryptocurrencytwelve
#from .capitalinformation.governmentincentiveseb576 import governmentincentiveseb5,governmentincentiveseb5faq,governmentincentiveseb5twelve
#from .capitalinformation.investmentbankingbrokersyndication77 import investmentbankingbrokersyndication,investmentbankingbrokersyndicationfaq,investmentbankingbrokersyndicationtwelve
#from .capitalinformation.privateequitysecuritiesaccreditedinvestors78 import privateequitysecuritiesaccreditedinvestors,privateequitysecuritiesaccreditedinvestorsfaq,privateequitysecuritiesaccreditedinvestorstwelve
#from .capitalinformation.venturecapitalshorttermbridgefinancing79 import venturecapitalshorttermbridgefinancing,venturecapitalshorttermbridgefinancingfaq,venturecapitalshorttermbridgefinancingtwelve
#from .capitalinformation.digitalcurrencytokenization80 import digitalcurrencytokenization,digitalcurrencytokenizationfaq,digitalcurrencytokenizationtwelve
#from .capitalinformation.privateequitysecuritiesprivateplacementmemorandum81 import privateequitysecuritiesprivateplacementmemorandum,privateequitysecuritiesprivateplacementmemorandumfaq,privateequitysecuritiesprivateplacementmemorandumtwelve
#from .capitalinformation.privateequitysecuritiesregulationa82 import privateequitysecuritiesregulationa,privateequitysecuritiesregulationafaq,privateequitysecuritiesregulationatwelve
#from .capitalinformation.privateequitysecuritiesregulationaplus83 import privateequitysecuritiesregulationaplus,privateequitysecuritiesregulationaplusfaq,privateequitysecuritiesregulationaplustwelve
#from .capitalinformation.privateequitysecuritiesregulationcftittleiii84 import privateequitysecuritiesregulationcftittleiii,privateequitysecuritiesregulationcftittleiiifaq,privateequitysecuritiesregulationcftittleiiitwelve
#from .capitalinformation.digitalcurrencyico85 import digitalcurrencyico,digitalcurrencyicofaq,digitalcurrencyicotwelve
#from .capitalinformation.digitalcurrencyieo86 import digitalcurrencyieo,digitalcurrencyieofaq,digitalcurrencyieotwelve
#from .capitalinformation.investmentbankingbrokerdealerrepresentation87 import investmentbankingbrokerdealerrepresentation,investmentbankingbrokerdealerrepresentationfaq,investmentbankingbrokerdealerrepresentationtwelve
#from .capitalinformation.investmentbankingequitysale88 import investmentbankingequitysale,investmentbankingequitysalefaq,investmentbankingequitysaletwelve
#from .capitalinformation.privateequitysecuritiesbrokerdealers89 import privateequitysecuritiesbrokerdealers,privateequitysecuritiesbrokerdealersfaq,privateequitysecuritiesbrokerdealerstwelve
#from .capitalinformation.publicsecuritiesderivatives90 import publicsecuritiesderivatives,publicsecuritiesderivativesfaq,publicsecuritiesderivativestwelve
#from .capitalinformation.publicsecuritiesspacspecialpurposeacquisitioncompany91 import publicsecuritiesspacspecialpurposeacquisitioncompany,publicsecuritiesspacspecialpurposeacquisitioncompanyfaq,publicsecuritiesspacspecialpurposeacquisitioncompanytwelve
#from .capitalinformation.venturecapitalmezzaninefinancing92 import venturecapitalmezzaninefinancing,venturecapitalmezzaninefinancingfaq,venturecapitalmezzaninefinancingtwelve
#from .capitalinformation.publicsecuritiesmarketmaker93 import publicsecuritiesmarketmaker,publicsecuritiesmarketmakerfaq,publicsecuritiesmarketmakertwelve
#from .capitalinformation.publicsecuritiesmoneymarketinstruments94 import publicsecuritiesmoneymarketinstruments,publicsecuritiesmoneymarketinstrumentsfaq,publicsecuritiesmoneymarketinstrumentstwelve
#from .capitalinformation.publicsecuritiespipeprivateinvestmentinpublicentity95 import publicsecuritiespipeprivateinvestmentinpublicentity,publicsecuritiespipeprivateinvestmentinpublicentityfaq,publicsecuritiespipeprivateinvestmentinpublicentitytwelve
#from .capitalinformation.venturecapitallongtermdebt96 import venturecapitallongtermdebt,venturecapitallongtermdebtfaq,venturecapitallongtermdebttwelve
#from .capitalinformation.publicsecuritiesinitialpublicofferingipo97 import publicsecuritiesinitialpublicofferingipo,publicsecuritiesinitialpublicofferingipofaq,publicsecuritiesinitialpublicofferingipotwelve
#from .capitalinformation.publicsecuritiesotcoverthecounter98 import publicsecuritiesotcoverthecounter,publicsecuritiesotcoverthecounterfaq,publicsecuritiesotcoverthecountertwelve
#from .capitalinformation.venturecapitalmergersacquisitionsfinancing99 import venturecapitalmergersacquisitionsfinancing,venturecapitalmergersacquisitionsfinancingfaq,venturecapitalmergersacquisitionsfinancingtwelve
#from .capitalinformation.venturecapitalequitysale100 import venturecapitalequitysale,venturecapitalequitysalefaq,venturecapitalequitysaletwelve

urlpatterns = [
    path('match/', Match, name='match'),
    path('word/',word,name='word'),
    path('pdf/',pdf,name='pdf'),
    path('definitions/',definition,name='definition'),
    path('twelvevairable/',twelvevariable,name='twelvevariable'),
    path('FAQ/',faq,name='FAQ'),
    path('summary-of-response/',summary,name='summary-of-response'),
    #path('owner-debt-cash-savings/', ownerdebtcashsaving, name='Owner Debt - Cash Savings'),
    #path('owner-debt-cash-savings-faq/', ownerdebtcashsavingfaq, name='Owner Debt - Cash Savingsfaq'),
    #path('owner-debt-cash-savings-twelve/', ownerdebtcashsavingtwelve, name='Owner Debt - Cash Savingstwelve'),
    #path('accelerator-university/', acceleratoruniversity, name='Accelerator University'),
    #path('accelerator-university-faq/', acceleratoruniversityfaq, name='Accelerator Universityfaq'),
    #path('accelerator-university-twelve/', acceleratoruniversitytwelve, name='Accelerator Universitytwelve'),
    #path('incubator-university/', incubatoruniversity, name='Incubator - University'),
    #path('incubator-university-faq/', incubatoruniversityfaq, name='Incubator - Universityfaq'),
    #path('incubator-university-twelve/', incubatoruniversitytwelve, name='Incubator - Universitytwelve'),
    #path('accelerator-public/', acceleratorpublic, name='Accelerator - Public'),
    #path('accelerator-public-faq/', acceleratorpublicfaq, name='Accelerator - Publicfaq'),
    #path('accelerator-public-twelve/', acceleratorpublictwelve, name='Accelerator - Publictwelve'),
    #path('incubator-public/', incubatorpublic, name='Incubator - Public'),
    #path('incubator-public-faq/', incubatorpublicfaq, name='Incubator - Publicfaq'),
    #path('incubator-public-twelve/', incubatorpublictwelve, name='Incubator - Publictwelve'),
    #path('small-business-administration-sba-sba-veteran/', smallbusinessadministrationsbasbaveteran, name='Small Business Administration (SBA) - SBA Veteran'),
    #path('small-business-administration-sba-sba-veteran-faq/', smallbusinessadministrationsbasbaveteranfaq, name='Small Business Administration (SBA) - SBA Veteranfaq'),
    #path('small-business-administration-sba-sba-veteran-twelve/', smallbusinessadministrationsbasbaveterantwelve, name='Small Business Administration (SBA) - SBA Veterantwelve'),
    #path('royalty-financing-top-line-revenue/', royaltyfinancingtoplinerevenue, name='Royalty Financing - Top Line Revenue'),
    #path('royalty-financing-top-line-revenue-faq/', royaltyfinancingtoplinerevenuefaq, name='Royalty Financing - Top Line Revenuefaq'),
    #path('royalty-financing-top-line-revenue-twelve/', royaltyfinancingtoplinerevenuetwelve, name='Royalty Financing - Top Line Revenuetwelve'),
    #path('grants-municipalities/', grantsmunicipalities, name='Grants - Municipalities'),
    #path('grants-municipalities-faq/', grantsmunicipalitiesfaq, name='Grants - Municipalitiesfaq'),
    #path('grants-municipalities-twelve/', grantsmunicipalitiestwelve, name='Grants - Municipalitiestwelve'),
    #path('owner-debt-whole-life-insurance/', ownerdebtwholelifeinsurance, name='Owner Debt - Whole Life Insurance'),
    #path('owner-debt-whole-life-insurance-faq/', ownerdebtwholelifeinsurancefaq, name='Owner Debt - Whole Life Insurancefaq'),
    #path('owner-debt-whole-life-insurance-twelve/', ownerdebtwholelifeinsurancetwelve, name='Owner Debt - Whole Life Insurancetwelve'),
    #path('private-equity-securities-safe/', privateequitysecuritiessafesimpleagreementfutureequity, name='Private Equity Securities - SAFE'),
    #path('private-equity-securities-safe-faq/', privateequitysecuritiessafesimpleagreementfutureequityfaq, name='Private Equity Securities - SAFEfaq'),
    #path('private-equity-securities-safe-twelve/', privateequitysecuritiessafesimpleagreementfutureequitytwelve, name='Private Equity Securities - SAFEtwelve'),
    #path('grants-government/', grantsgovernment, name='Grants - Government'),
    #path('grants-government-faq/', grantsgovernmentfaq, name='Grants - Governmentfaq'),
    #path('grants-government-twelve/', grantsgovernmenttwelve, name='Grants - Governmenttwelve'),
    #path('owner-debt-home-equity/', ownerdebthomeequity, name='Owner Debt - Home Equity'),
    #path('owner-debt-home-equity-faq/', ownerdebthomeequityfaq, name='Owner Debt - Home Equityfaq'),
    #path('owner-debt-home-equity-twelve/', ownerdebthomeequitytwelve, name='Owner Debt - Home Equitytwelve'),
    #path('small-business-administration-sba-sba-express/', smallbusinessadministrationsbasbaexpress, name='Small Business Administration (SBA) - SBA Express'),
    #path('small-business-administration-sba-sba-express-faq/', smallbusinessadministrationsbasbaexpressfaq, name='Small Business Administration (SBA) - SBA Expressfaq'),
    #path('small-business-administration-sba-sba-express-twelve/', smallbusinessadministrationsbasbaexpresstwelve, name='Small Business Administration (SBA) - SBA Expresstwelve'),
    #path('accelerator-private/', acceleratorprivate, name='Accelerator - Private'),
    #path('accelerator-private-faq/', acceleratorprivatefaq, name='Accelerator - Privatefaq'),
    #path('accelerator-private-twelve/', acceleratorprivatetwelve, name='Accelerator - Privatetwelve'),
    #path('commercial-banking-equipment-loan/', commercialbankingequipmentloan, name='Commercial Banking - Equipment Loan'),
    #path('commercial-banking-equipment-loan-faq/', commercialbankingequipmentloanfaq, name='Commercial Banking - Equipment Loanfaq'),
    #path('commercial-banking-equipment-loan-twelve/', commercialbankingequipmentloantwelve, name='Commercial Banking - Equipment Loantwelve'),
    #path('commercial-banking-standby-letter-of-credit-sblc/', commercialbankingsblc, name='Commercial Banking - Standby Letter of Credit (SBLC)'),
    #path('commercial-banking-standby-letter-of-credit-sblc-faq/', commercialbankingsblcfaq, name='Commercial Banking - Standby Letter of Credit (SBLC)faq'),
    #path('commercial-banking-standby-letter-of-credit-sblc-twelve/', commercialbankingsblctwelve, name='Commercial Banking - Standby Letter of Credit (SBLC)twelve'),
    #path('grants-education-grants/', grantseducation, name='Grants - Education Grants'),
    #path('grants-education-grants-faq/', grantseducationfaq, name='Grants - Education Grantsfaq'),
    #path('grants-education-grants-twelve/', grantseducationtwelve, name='Grants - Education Grantstwelve'),
    #path('grants-state-agencies/', grantsstateagencies, name='Grants - State Agencies'),
    #path('grants-state-agencies-faq/', grantsstateagenciesfaq, name='Grants - State Agenciesfaq'),
    #path('grants-state-agencies-twelve/', grantsstateagenciestwelve, name='Grants - State Agenciestwelve'),
    #path('incubator-private/', incubatorprivate, name='Incubator - Private'),
    #path('incubator-private-faq/', incubatorprivatefaq, name='Incubator - Privatefaq'),
    #path('incubator-private-twelve/', incubatorprivatetwelve, name='Incubator - Privatetwelve'),
    #path('small-business-administration-sba-sbic/', smallbusinessadministrationsbasbic, name='Small Business Administration (SBA) - SBIC'),
    #path('small-business-administration-sba-sbic-faq/', smallbusinessadministrationsbasbicfaq, name='Small Business Administration (SBA) - SBICfaq'),
    #path('small-business-administration-sba-sbic-twelve/', smallbusinessadministrationsbasbictwelve, name='Small Business Administration (SBA) - SBICtwelve'),
    #path('commercial-banking-line-of-credit/', commercialbankinglineofcredit, name='Commercial Banking - Line of Credit'),
    #path('commercial-banking-line-of-credit-faq/', commercialbankinglineofcreditfaq, name='Commercial Banking - Line of Creditfaq'),
    #path('commercial-banking-line-of-credit-twelve/', commercialbankinglineofcredittwelve, name='Commercial Banking - Line of Credittwelve'),
    #path('commercial-banking-real-estate-loan/', commercialbankingrealestate, name='Commercial Banking - Real Estate Loan'),
    #path('commercial-banking-real-estate-loan-faq/', commercialbankingrealestatefaq, name='Commercial Banking - Real Estate Loanfaq'),
    #path('commercial-banking-real-estate-loan-twelve/', commercialbankingrealestatetwelve, name='Commercial Banking - Real Estate Loantwelve'),
    #path('government-incentives-opportunity-zone-tax-credit-fund/', governmentincentivesopportunityzone, name='Government Incentives Opportunity Zone Tax Credit Fund'),
    #path('government-incentives-opportunity-zone-tax-credit-fund-faq/', governmentincentivesopportunityzonefaq, name='Government Incentives Opportunity Zone Tax Credit Fundfaq'),
    #path('government-incentives-opportunity-zone-tax-credit-fund-twelve/', governmentincentivesopportunityzonetwelve, name='Government Incentives Opportunity Zone Tax Credit Fundtwelve'),
    #path('owner-debt-retirement-401k-sdi/', ownerdebtretirement401ksdi, name='Owner Debt - Retirement (401K) SDI'),
    #path('owner-debt-retirement-401k-sdi-faq/', ownerdebtretirement401ksdifaq, name='Owner Debt - Retirement (401K) SDIfaq'),
    #path('owner-debt-retirement-401k-sdi-twelve/', ownerdebtretirement401ksditwelve, name='Owner Debt - Retirement (401K) SDItwelve'),
    #path('private-equity-securities-family-and-friends/', privateequitysecuritiesfamilyfriends, name='Private Equity Securities - Family & Friends'),
    #path('private-equity-securities-family-and-friends-faq/', privateequitysecuritiesfamilyfriendsfaq, name='Private Equity Securities - Family & Friendsfaq'),
    #path('private-equity-securities-family-and-friends-twelve/', privateequitysecuritiesfamilyfriendstwelve, name='Private Equity Securities - Family & Friendstwelve'),
    #path('small-business-administration-sba-sba-504b/', smallbusinessadministrationsbasba504b, name='Small Business Administration (SBA) - SBA 504B'),
    #path('small-business-administration-sba-sba-504b-faq/', smallbusinessadministrationsbasba504bfaq, name='Small Business Administration (SBA) - SBA 504Bfaq'),
    #path('small-business-administration-sba-sba-504b-twelve/', smallbusinessadministrationsbasba504btwelve, name='Small Business Administration (SBA) - SBA 504Btwelve'),
    #path('small-business-administration-sba-sba-7a/', smallbusinessadministrationsbasba7a, name='Small Business Administration (SBA) - SBA 7A'),
    #path('small-business-administration-sba-sba-7a-faq/', smallbusinessadministrationsbasba7afaq, name='Small Business Administration (SBA) - SBA 7Afaq'),
    #path('small-business-administration-sba-sba-7a-twelve/', smallbusinessadministrationsbasba7atwelve, name='Small Business Administration (SBA) - SBA 7Atwelve'),
    #path('commercial-banking-commercial-bank-loan/', commercialbankingcommercialbankloann, name='Commercial Banking - Commercial Bank Loan'),
    #path('commercial-banking-commercial-bank-loan-faq/', commercialbankingcommercialbankloannfaq, name='Commercial Banking - Commercial Bank Loanfaq'),
    #path('commercial-banking-commercial-bank-loan-twelve/', commercialbankingcommercialbankloanntwelve, name='Commercial Banking - Commercial Bank Loantwelve'),
    #path('government-incentives-enterprise-zones/', governmentincentivesenterprisezones, name='Government Incentives - Enterprise Zones'),
    #path('government-incentives-enterprise-zones-faq/', governmentincentivesenterprisezonesfaq, name='Government Incentives - Enterprise Zonesfaq'),
    #path('government-incentives-enterprise-zones-twelve/', governmentincentivesenterprisezonestwelve, name='Government Incentives - Enterprise Zonestwelve'),
    #path('commercial-banking-acquisition-loan/', commercialbankingacquisitionloan, name='Commercial Banking - Acquisition Loan'),
    #path('commercial-banking-acquisition-loan-faq/', commercialbankingacquisitionloanfaq, name='Commercial Banking - Acquisition Loanfaq'),
    #path('commercial-banking-acquisition-loan-twelve/', commercialbankingacquisitionloantwelve, name='Commercial Banking - Acquisition Loantwelve'),
    #path('grants-research-grants/', grantsresearch, name='Grants - Research Grants'),
    #path('grants-research-grants-faq/', grantsresearchfaq, name='Grants - Research Grantsfaq'),
    #path('grants-research-grants-twelve/', grantsresearchtwelve, name='Grants - Research Grantstwelve'),
    #path('owner-debt-personal-credit-cards/', ownerdebtpersonalcreditcards, name='Owner Debt - Personal Credit Cards'),
    #path('owner-debt-personal-credit-cards-faq/', ownerdebtpersonalcreditcardsfaq, name='Owner Debt - Personal Credit Cardsfaq'),
    #path('owner-debt-personal-credit-cards-twelve/', ownerdebtpersonalcreditcardstwelve, name='Owner Debt - Personal Credit Cardstwelve'),
    #path('small-business-administration-sba-cdc-sbdc/', smallbusinessadministrationsbacdcsbdc, name='Small Business Administration (SBA) - CDC/SBDC'),
    #path('small-business-administration-sba-cdc-sbdc-faq/', smallbusinessadministrationsbacdcsbdcfaq, name='Small Business Administration (SBA) - CDC/SBDCfaq'),
    #path('small-business-administration-sba-cdc-sbdc-twelve/', smallbusinessadministrationsbacdcsbdctwelve, name='Small Business Administration (SBA) - CDC/SBDCtwelve'),
    #path('commercial-banking-asset-based-lending/', commercialbankingassetbasedlending, name='Commercial Banking - Asset Based Lending'),
    #path('commercial-banking-asset-based-lending-faq/', commercialbankingassetbasedlendingfaq, name='Commercial Banking - Asset Based Lendingfaq'),
    #path('commercial-banking-asset-based-lending-twelve/', commercialbankingassetbasedlendingtwelve, name='Commercial Banking - Asset Based Lendingtwelve'),
    #path('owner-debt-personal-resources-or-loans/', ownerdebtpersonalresourcesorloans, name='Owner Debt - Personal Resources or Loans'),
    #path('owner-debt-personal-resources-or-loans-faq/', ownerdebtpersonalresourcesorloansfaq, name='Owner Debt - Personal Resources or Loansfaq'),
    #path('owner-debt-personal-resources-or-loans-twelve/', ownerdebtpersonalresourcesorloanstwelve, name='Owner Debt - Personal Resources or Loanstwelve'),
    #path('private-debt-promissory-note/', privatedebtpromissorynote, name='Private Debt - Promissory Note'),
    #path('private-debt-promissory-note-faq/', privatedebtpromissorynotefaq, name='Private Debt - Promissory Notefaq'),
    #path('private-debt-promissory-note-twelve/', privatedebtpromissorynotetwelve, name='Private Debt - Promissory Notetwelve'),
    #path('commercial-banking-collateralized-debt/', commercialbankingcollateralizeddebt, name='Commercial Banking - Collateralized Debt'),
    #path('commercial-banking-collateralized-debt-faq/', commercialbankingcollateralizeddebtfaq, name='Commercial Banking - Collateralized Debtfaq'),
    #path('commercial-banking-collateralized-debt-twelve/', commercialbankingcollateralizeddebttwelve, name='Commercial Banking - Collateralized Debttwelve'),
    #path('private-debt-real-estate-loan/', privatedebtrealestateloan, name='Private Debt - Real Estate Loan'),
    #path('private-debt-real-estate-loan-faq/', privatedebtrealestateloanfaq, name='Private Debt - Real Estate Loanfaq'),
    #path('private-debt-real-estate-loan-twelve/', privatedebtrealestateloantwelve, name='Private Debt - Real Estate Loantwelve'),
    #path('private-equity-securities-family-offices/', privateequitysecuritiesfamilyoffices, name='Private Equity Securities - Family Offices'),
    #path('private-equity-securities-family-offices-faq/', privateequitysecuritiesfamilyofficesfaq, name='Private Equity Securities - Family Officesfaq'),
    #path('private-equity-securities-family-offices-twelve/', privateequitysecuritiesfamilyofficestwelve, name='Private Equity Securities - Family Officestwelve'),
    #path('private-debt-asset-based-lending/', privatedebtassetbasedlending, name='Private Debt - Asset Based Lending'),
    #path('private-debt-asset-based-lending-faq/', privatedebtassetbasedlendingfaq, name='Private Debt - Asset Based Lendingfaq'),
    #path('private-debt-asset-based-lending-twelve/', privatedebtassetbasedlendingtwelve, name='Private Debt - Asset Based Lendingtwelve'),
    #path('private-debt-bridge-financing/', privatedebtbridgefinancing, name='Private Debt - Bridge Financing'),
    #path('private-debt-bridge-financing-faq/', privatedebtbridgefinancingfaq, name='Private Debt - Bridge Financingfaq'),
    #path('private-debt-bridge-financing-twelve/', privatedebtbridgefinancingtwelve, name='Private Debt - Bridge Financingtwelve'),
    #path('private-debt-private-debt/', privatedebtprivatedebt, name='Private Debt - Private Debt'),
    #path('private-debt-private-debt-faq/', privatedebtprivatedebtfaq, name='Private Debt - Private Debtfaq'),
    #path('private-debt-private-debt-twelve/', privatedebtprivatedebttwelve, name='Private Debt - Private Debttwelve'),
    #path('alternative-apps-ie-cabbage/', alternativeapps, name='Alternative - Apps (i.e. Cabbage)'),
    #path('alternative-apps-ie-cabbage-faq/', alternativeappsfaq, name='Alternative - Apps (i.e. Cabbage)faq'),
    #path('alternative-apps-ie-cabbage-twelve/', alternativeappstwelve, name='Alternative - Apps (i.e. Cabbage)twelve'),
    #path('commercial-banking-credit-card/', commercialbankingcreditcard, name='Commercial Banking - Credit Card'),
    #path('commercial-banking-credit-card-faq/', commercialbankingcreditcardfaq, name='Commercial Banking - Credit Cardfaq'),
    #path('commercial-banking-credit-card-twelve/', commercialbankingcreditcardtwelve, name='Commercial Banking - Credit Cardtwelve'),
    #path('digital-currency-investment-via-crypto-wallet/', digitalcurrencycryptowallet, name='Digital Currency - Investment via Crypto Wallet'),
    #path('digital-currency-investment-via-crypto-wallet-faq/', digitalcurrencycryptowalletfaq, name='Digital Currency - Investment via Crypto Walletfaq'),
    #path('digital-currency-investment-via-crypto-wallet-twelve/', digitalcurrencycryptowallettwelve, name='Digital Currency - Investment via Crypto Wallettwelve'),
    #path('private-equity-securities-angel-investors/', privateequitysecuritiesangelinvestors, name='Private Equity Securities - Angel Investors'),
    #path('private-equity-securities-angel-investors-faq/', privateequitysecuritiesangelinvestorsfaq, name='Private Equity Securities - Angel Investorsfaq'),
    #path('private-equity-securities-angel-investors-twelve/', privateequitysecuritiesangelinvestorstwelve, name='Private Equity Securities - Angel Investorstwelve'),
    #path('private-equity-securities-convertible-note/', privateequitysecuritiesconvertiblenote, name='Private Equity Securities - Convertible Note'),
    #path('private-equity-securities-convertible-note-faq/', privateequitysecuritiesconvertiblenotefaq, name='Private Equity Securities - Convertible Notefaq'),
    #path('private-equity-securities-convertible-note-twelve/', privateequitysecuritiesconvertiblenotetwelve, name='Private Equity Securities - Convertible Notetwelve'),
    #path('grants-corporate-grants/', grantscorporate, name='Grants - Corporate Grants'),
    #path('grants-corporate-grants-faq/', grantscorporatefaq, name='Grants - Corporate Grantsfaq'),
    #path('grants-corporate-grants-twelve/', grantscorporatetwelve, name='Grants - Corporate Grantstwelve'),
    #path('private-debt-acquisition-loan/', privatedebtacquisitionloan, name='Private Debt - Acquisition Loan'),
    #path('private-debt-acquisition-loan-faq/', privatedebtacquisitionloanfaq, name='Private Debt - Acquisition Loanfaq'),
    #path('private-debt-acquisition-loan-twelve/', privatedebtacquisitionloantwelve, name='Private Debt - Acquisition Loantwelve'),
    #path('private-debt-hard-money-loan/', privatedebthardmoneyloan, name='Private Debt - Hard Money Loan'),
    #path('private-debt-hard-money-loan-faq/', privatedebthardmoneyloanfaq, name='Private Debt - Hard Money Loanfaq'),
    #path('private-debt-hard-money-loan-twelve/', privatedebthardmoneyloantwelve, name='Private Debt - Hard Money Loantwelve'),
    #path('alternative-corporate-credit-third-party/', alternativecorporatecredit, name='Alternative - Corporate Credit (Third Party)'),
    #path('alternative-corporate-credit-third-party-faq/', alternativecorporatecreditfaq, name='Alternative - Corporate Credit (Third Party)faq'),
    #path('alternative-corporate-credit-third-party-twelve/', alternativecorporatecredittwelve, name='Alternative - Corporate Credit (Third Party)twelve'),
    #path('factoring-accounts-receivable-loans/', factoringaccountsreceivable, name='Factoring - Accounts Receivable Loans'),
    #path('factoring-accounts-receivable-loans-faq/', factoringaccountsreceivablefaq, name='Factoring - Accounts Receivable Loansfaq'),
    #path('factoring-accounts-receivable-loans-twelve/', factoringaccountsreceivabletwelve, name='Factoring - Accounts Receivable Loanstwelve'),
    #path('factoring-merchant-account-advances/', factoringmerchantaccount, name='Factoring - Merchant Account Advances'),
    #path('factoring-merchant-account-advances-faq/', factoringmerchantaccountfaq, name='Factoring - Merchant Account Advancesfaq'),
    #path('factoring-merchant-account-advances-twelve/', factoringmerchantaccounttwelve, name='Factoring - Merchant Account Advancestwelve'),
    #path('bonds-government-backed/', bondsgovernmentbacked, name='Bonds - Government Backed'),
    #path('bonds-government-backed-faq/', bondsgovernmentbackedfaq, name='Bonds - Government Backedfaq'),
    #path('bonds-government-backed-twelve/', bondsgovernmentbackedtwelve, name='Bonds - Government Backedtwelve'),
    #path('bonds-high-yield-junk/', bondshighyieldjunk, name='Bonds - High Yield Junk'),
    #path('bonds-high-yield-junk-faq/', bondshighyieldjunkfaq, name='Bonds - High Yield Junkfaq'),
    #path('bonds-high-yield-junk-twelve/', bondshighyieldjunktwelve, name='Bonds - High Yield Junktwelve'),
    #path('bonds-mortgage-backed/', bondsmortgagebacked, name='Bonds - Mortgage Backed'),
    #path('bonds-mortgage-backed-faq/', bondsmortgagebackedfaq, name='Bonds - Mortgage Backedfaq'),
    #path('bonds-mortgage-backed-twelve/', bondsmortgagebackedtwelve, name='Bonds - Mortgage Backedtwelve'),
    #path('factoring-purchase-order-loan/', factoringpurchaseorder, name='Factoring - Purchase Order Loan'),
    #path('factoring-purchase-order-loan-faq/', factoringpurchaseorderfaq, name='Factoring - Purchase Order Loanfaq'),
    #path('factoring-purchase-order-loan-twelve/', factoringpurchaseordertwelve, name='Factoring - Purchase Order Loantwelve'),
    #path('private-debt-collateralized-debt/', privatedebtcollateralizeddebt, name='Private Debt - Collateralized Debt'),
    #path('private-debt-collateralized-debt-faq/', privatedebtcollateralizeddebtfaq, name='Private Debt - Collateralized Debtfaq'),
    #path('private-debt-collateralized-debt-twelve/', privatedebtcollateralizeddebttwelve, name='Private Debt - Collateralized Debttwelve'),
    #path('factoring-invoice-factoring/', factoringinvoice, name='Factoring - Invoice Factoring'),
    #path('factoring-invoice-factoring-faq/', factoringinvoicefaq, name='Factoring - Invoice Factoringfaq'),
    #path('factoring-invoice-factoring-twelve/', factoringinvoicetwelve, name='Factoring - Invoice Factoringtwelve'),
    #path('government-incentives-gold-star/', governmentincentivesgoldstar, name='Government Incentives - Gold Star'),
    #path('government-incentives-gold-star-faq/', governmentincentivesgoldstarfaq, name='Government Incentives - Gold Starfaq'),
    #path('government-incentives-gold-star-twelve/', governmentincentivesgoldstartwelve, name='Government Incentives - Gold Startwelve'),
    #path('hedge-funds-public/', hedgefundspublic, name='Hedge Funds - Public'),
    #path('hedge-funds-public-faq/', hedgefundspublicfaq, name='Hedge Funds - Publicfaq'),
    #path('hedge-funds-public-twelve/', hedgefundspublictwelve, name='Hedge Funds - Publictwelve'),
    #path('investment-banking-mezzanine-financing/', investmentbankingmezzaninefinancing, name='Investment Banking - Mezzanine Financing'),
    #path('investment-banking-mezzanine-financing-faq/', investmentbankingmezzaninefinancingfaq, name='Investment Banking - Mezzanine Financingfaq'),
    #path('investment-banking-mezzanine-financing-twelve/', investmentbankingmezzaninefinancingtwelve, name='Investment Banking - Mezzanine Financingtwelve'),
    #path('private-equity-securities-regulation-d-506b/', privateequitysecuritiesregulationd506b, name='Private Equity Securities - Regulation D 506(b)'),
    #path('private-equity-securities-regulation-d-506b-faq/', privateequitysecuritiesregulationd506bfaq, name='Private Equity Securities - Regulation D 506(b)faq'),
    #path('private-equity-securities-regulation-d-506b-twelve/', privateequitysecuritiesregulationd506btwelve, name='Private Equity Securities - Regulation D 506(b)twelve'),
    #path('digital-currency-stable-coins-dao-blockchain/', digitalcurrencystablecoins, name='Digital Currency - Stable Coins (DAO) - Blockchain'),
    #path('digital-currency-stable-coins-dao-blockchain-faq/', digitalcurrencystablecoinsfaq, name='Digital Currency - Stable Coins (DAO) - Blockchainfaq'),
    #path('digital-currency-stable-coins-dao-blockchain-twelve/', digitalcurrencystablecoinstwelve, name='Digital Currency - Stable Coins (DAO) - Blockchaintwelve'),
    #path('bonds-foreign/', bondsforeign, name='Bonds - Foreign'),
    #path('bonds-foreign-faq/', bondsforeignfaq, name='Bonds - Foreignfaq'),
    #path('bonds-foreign-twelve/', bondsforeigntwelve, name='Bonds - Foreigntwelve'),
    #path('private-equity-securities-regulation-d-506c/', privateequitysecuritiesregulationd506c, name='Private Equity Securities - Regulation D 506(c)'),
    #path('private-equity-securities-regulation-d-506c-faq/', privateequitysecuritiesregulationd506cfaq, name='Private Equity Securities - Regulation D 506(c)faq'),
    #path('private-equity-securities-regulation-d-506c-twelve/', privateequitysecuritiesregulationd506ctwelve, name='Private Equity Securities - Regulation D 506(c)twelve'),
    #path('private-equity-securities-rule-144/', privateequitysecuritiesrule144, name='Private Equity Securities - Rule 144'),
    #path('private-equity-securities-rule-144-faq/', privateequitysecuritiesrule144faq, name='Private Equity Securities - Rule 144faq'),
    #path('private-equity-securities-rule-144-twelve/', privateequitysecuritiesrule144twelve, name='Private Equity Securities - Rule 144twelve'),
    #path('alternative-high-yield-business-consumer-loan/', alternativehighyield, name='Alternative - High Yield Business Consumer Loan'),
    #path('alternative-high-yield-business-consumer-loan-faq/', alternativehighyieldfaq, name='Alternative - High Yield Business Consumer Loanfaq'),
    #path('alternative-high-yield-business-consumer-loan-twelve/', alternativehighyieldtwelve, name='Alternative - High Yield Business Consumer Loantwelve'),
    #path('investment-banking-investment-banker-debt/', investmentbankinginvestmentbankerdebt, name='Investment Banking - Investment Banker Debt'),
    #path('investment-banking-investment-banker-debt-faq/', investmentbankinginvestmentbankerdebtfaq, name='Investment Banking - Investment Banker Debtfaq'),
    #path('investment-banking-investment-banker-debt-twelve/', investmentbankinginvestmentbankerdebttwelve, name='Investment Banking - Investment Banker Debttwelve'),
    #path('private-equity-securities-regulation-d-505/', privateequitysecuritiesregulationd505, name='Private Equity Securities - Regulation D 505'),
    #path('private-equity-securities-regulation-d-505-faq/', privateequitysecuritiesregulationd505faq, name='Private Equity Securities - Regulation D 505faq'),
    #path('private-equity-securities-regulation-d-505-twelve/', privateequitysecuritiesregulationd505twelve, name='Private Equity Securities - Regulation D 505twelve'),
    #path('private-equity-securities-sophisticated-individuals/', privateequitysecuritiessophisticatedindividuals, name='Private Equity Securities - Sophisticated Individuals'),
    #path('private-equity-securities-sophisticated-individuals-faq/', privateequitysecuritiessophisticatedindividualsfaq, name='Private Equity Securities - Sophisticated Individualsfaq'),
    #path('private-equity-securities-sophisticated-individuals-twelve/', privateequitysecuritiessophisticatedindividualstwelve, name='Private Equity Securities - Sophisticated Individualstwelve'),
    #path('bonds-investment-grade/', bondsinvestmentgrade, name='Bonds - Investment Grade'),
    #path('bonds-investment-grade-faq/', bondsinvestmentgradefaq, name='Bonds - Investment Gradefaq'),
    #path('bonds-investment-grade-twelve/', bondsinvestmentgradetwelve, name='Bonds - Investment Gradetwelve'),
    #path('hedge-funds-private/', hedgefundsprivate, name='Hedge Funds - Private'),
    #path('hedge-funds-private-faq/', hedgefundsprivatefaq, name='Hedge Funds - Privatefaq'),
    #path('hedge-funds-private-twelve/', hedgefundsprivatetwelve, name='Hedge Funds - Privatetwelve'),
    #path('private-equity-securities-regulation-d-504/', privateequitysecuritiesregulationd504, name='Private Equity Securities - Regulation D 504'),
    #path('private-equity-securities-regulation-d-504-faq/', privateequitysecuritiesregulationd504faq, name='Private Equity Securities - Regulation D 504faq'),
    #path('private-equity-securities-regulation-d-504-twelve/', privateequitysecuritiesregulationd504twelve, name='Private Equity Securities - Regulation D 504twelve'),
    #path('digital-currency-cryptocurrency/', digitalcurrencycryptocurrency, name='Digital Currency - Cryptocurrency'),
    #path('digital-currency-cryptocurrency-faq/', digitalcurrencycryptocurrencyfaq, name='Digital Currency - Cryptocurrencyfaq'),
    #path('digital-currency-cryptocurrency-twelve/', digitalcurrencycryptocurrencytwelve, name='Digital Currency - Cryptocurrencytwelve'),
    #path('government-incentives-eb5-immigration/', governmentincentiveseb5, name='Government Incentives - EB5 Immigration'),
    #path('government-incentives-eb5-immigration-faq/', governmentincentiveseb5faq, name='Government Incentives - EB5 Immigrationfaq'),
    #path('government-incentives-eb5-immigration-twelve/', governmentincentiveseb5twelve, name='Government Incentives - EB5 Immigrationtwelve'),
    #path('investment-banking-broker-syndication/', investmentbankingbrokersyndication, name='Investment Banking - Broker Syndication'),
    #path('investment-banking-broker-syndication-faq/', investmentbankingbrokersyndicationfaq, name='Investment Banking - Broker Syndicationfaq'),
    #path('investment-banking-broker-syndication-twelve/', investmentbankingbrokersyndicationtwelve, name='Investment Banking - Broker Syndicationtwelve'),
    #path('private-equity-securities-accredited-investors/', privateequitysecuritiesaccreditedinvestors, name='Private Equity Securities - Accredited Investors'),
    #path('private-equity-securities-accredited-investors-faq/', privateequitysecuritiesaccreditedinvestorsfaq, name='Private Equity Securities - Accredited Investorsfaq'),
    #path('private-equity-securities-accredited-investors-twelve/', privateequitysecuritiesaccreditedinvestorstwelve, name='Private Equity Securities - Accredited Investorstwelve'),
    #path('venture-capital-short-term-bridge-financing/', venturecapitalshorttermbridgefinancing, name='Venture Capital - Short-Term Bridge Financing'),
    #path('venture-capital-short-term-bridge-financing-faq/', venturecapitalshorttermbridgefinancingfaq, name='Venture Capital - Short-Term Bridge Financingfaq'),
    #path('venture-capital-short-term-bridge-financing-twelve/', venturecapitalshorttermbridgefinancingtwelve, name='Venture Capital - Short-Term Bridge Financingtwelve'),
    #path('digital-currency-tokenization/', digitalcurrencytokenization, name='Digital Currency - Tokenization'),
    #path('digital-currency-tokenization-faq/', digitalcurrencytokenizationfaq, name='Digital Currency - Tokenizationfaq'),
    #path('digital-currency-tokenization-twelve/', digitalcurrencytokenizationtwelve, name='Digital Currency - Tokenizationtwelve'),
    #path('private-equity-securities-private-placement-memorandum/', privateequitysecuritiesprivateplacementmemorandum, name='Private Equity Securities - Private Placement Memorandum'),
    #path('private-equity-securities-private-placement-memorandum-faq/', privateequitysecuritiesprivateplacementmemorandumfaq, name='Private Equity Securities - Private Placement Memorandumfaq'),
    #path('private-equity-securities-private-placement-memorandum-twelve/', privateequitysecuritiesprivateplacementmemorandumtwelve, name='Private Equity Securities - Private Placement Memorandumtwelve'),
    #path('private-equity-securities-regulation-a/', privateequitysecuritiesregulationa, name='Private Equity Securities - Regulation A'),
    #path('private-equity-securities-regulation-a-faq/', privateequitysecuritiesregulationafaq, name='Private Equity Securities - Regulation Afaq'),
    #path('private-equity-securities-regulation-a-twelve/', privateequitysecuritiesregulationatwelve, name='Private Equity Securities - Regulation Atwelve'),
    #path('private-equity-securities-regulation-aplus/', privateequitysecuritiesregulationaplus, name='Private Equity Securities - Regulation A+'),
    #path('private-equity-securities-regulation-aplus-faq/', privateequitysecuritiesregulationaplusfaq, name='Private Equity Securities - Regulation A+faq'),
    #path('private-equity-securities-regulation-aplus-twelve/', privateequitysecuritiesregulationaplustwelve, name='Private Equity Securities - Regulation A+twelve'),
    #path('private-equity-securities-regulation-cf-tittle-iii/', privateequitysecuritiesregulationcftittleiii, name='Private Equity Securities - Regulation CF Tittle III'),
    #path('private-equity-securities-regulation-cf-tittle-iii-faq/', privateequitysecuritiesregulationcftittleiiifaq, name='Private Equity Securities - Regulation CF Tittle IIIfaq'),
    #path('private-equity-securities-regulation-cf-tittle-iii-twelve/', privateequitysecuritiesregulationcftittleiiitwelve, name='Private Equity Securities - Regulation CF Tittle IIItwelve'),
    #path('digital-currency-initial-coin-offering/', digitalcurrencyico, name='Digital Currency - Initial Coin Offering'),
    #path('digital-currency-initial-coin-offering-faq/', digitalcurrencyicofaq, name='Digital Currency - Initial Coin Offeringfaq'),
    #path('digital-currency-initial-coin-offering-twelve/', digitalcurrencyicotwelve, name='Digital Currency - Initial Coin Offeringtwelve'),
    #path('digital-currency-initial-exchange-offering/', digitalcurrencyieo, name='Digital Currency - Initial Exchange Offering'),
    #path('digital-currency-initial-exchange-offering-faq/', digitalcurrencyieofaq, name='Digital Currency - Initial Exchange Offeringfaq'),
    #path('digital-currency-initial-exchange-offering-twelve/', digitalcurrencyieotwelve, name='Digital Currency - Initial Exchange Offeringtwelve'),
    #path('investment-banking-broker-dealer-representation/', investmentbankingbrokerdealerrepresentation, name='Investment Banking - Broker Dealer Representation'),
    #path('investment-banking-broker-dealer-representation-faq/', investmentbankingbrokerdealerrepresentationfaq, name='Investment Banking - Broker Dealer Representationfaq'),
    #path('investment-banking-broker-dealer-representation-twelve/', investmentbankingbrokerdealerrepresentationtwelve, name='Investment Banking - Broker Dealer Representationtwelve'),
    #path('investment-banking-equity-sale/', investmentbankingequitysale, name='Investment Banking - Equity Sale'),
    #path('investment-banking-equity-sale-faq/', investmentbankingequitysalefaq, name='Investment Banking - Equity Salefaq'),
    #path('investment-banking-equity-sale-twelve/', investmentbankingequitysaletwelve, name='Investment Banking - Equity Saletwelve'),
    #path('private-equity-securities-broker-dealers/', privateequitysecuritiesbrokerdealers, name='Private Equity Securities - Broker Dealers'),
    #path('private-equity-securities-broker-dealers-faq/', privateequitysecuritiesbrokerdealersfaq, name='Private Equity Securities - Broker Dealersfaq'),
    #path('private-equity-securities-broker-dealers-twelve/', privateequitysecuritiesbrokerdealerstwelve, name='Private Equity Securities - Broker Dealerstwelve'),
    #path('public-securities-derivatives/', publicsecuritiesderivatives, name='Public Securities - Derivatives'),
    #path('public-securities-derivatives-faq/', publicsecuritiesderivativesfaq, name='Public Securities - Derivativesfaq'),
    #path('public-securities-derivatives-twelve/', publicsecuritiesderivativestwelve, name='Public Securities - Derivativestwelve'),
    #path('public-securities-spac/', publicsecuritiesspacspecialpurposeacquisitioncompany, name='Public Securities - SPAC'),
    #path('public-securities-spac-faq/', publicsecuritiesspacspecialpurposeacquisitioncompanyfaq, name='Public Securities - SPACfaq'),
    #path('public-securities-spac-twelve/', publicsecuritiesspacspecialpurposeacquisitioncompanytwelve, name='Public Securities - SPACtwelve'),
    #path('venture-capital-mezzanine-financing/', venturecapitalmezzaninefinancing, name='Venture Capital - Mezzanine Financing'),
    #path('venture-capital-mezzanine-financing-faq/', venturecapitalmezzaninefinancingfaq, name='Venture Capital - Mezzanine Financingfaq'),
    #path('venture-capital-mezzanine-financing-twelve/', venturecapitalmezzaninefinancingtwelve, name='Venture Capital - Mezzanine Financingtwelve'),
    #path('public-securities-market-maker/', publicsecuritiesmarketmaker, name='Public Securities - Market Maker'),
    #path('public-securities-market-maker-faq/', publicsecuritiesmarketmakerfaq, name='Public Securities - Market Makerfaq'),
    #path('public-securities-market-maker-twelve/', publicsecuritiesmarketmakertwelve, name='Public Securities - Market Makertwelve'),
    #path('public-securities-money-market-instruments/', publicsecuritiesmoneymarketinstruments, name='Public Securities - Money Market Instruments'),
    #path('public-securities-money-market-instruments-faq/', publicsecuritiesmoneymarketinstrumentsfaq, name='Public Securities - Money Market Instrumentsfaq'),
    #path('public-securities-money-market-instruments-twelve/', publicsecuritiesmoneymarketinstrumentstwelve, name='Public Securities - Money Market Instrumentstwelve'),
    #path('public-securities-pipe/', publicsecuritiespipeprivateinvestmentinpublicentity, name='Public Securities - PIPE'),
    #path('public-securities-pipe-faq/', publicsecuritiespipeprivateinvestmentinpublicentityfaq, name='Public Securities - PIPEfaq'),
    #path('public-securities-pipe-twelve/', publicsecuritiespipeprivateinvestmentinpublicentitytwelve, name='Public Securities - PIPEtwelve'),
    #path('venture-capital-long-term-debt/', venturecapitallongtermdebt, name='Venture Capital - Long Term Debt'),
    #path('venture-capital-long-term-debt-faq/', venturecapitallongtermdebtfaq, name='Venture Capital - Long Term Debtfaq'),
    #path('venture-capital-long-term-debt-twelve/', venturecapitallongtermdebttwelve, name='Venture Capital - Long Term Debttwelve'),
    #path('public-securities-initial-public-offering-ipo/', publicsecuritiesinitialpublicofferingipo, name='Public Securities - Initial Public Offering (IPO)'),
    #path('public-securities-initial-public-offering-ipo-faq/', publicsecuritiesinitialpublicofferingipofaq, name='Public Securities - Initial Public Offering (IPO)faq'),
    #path('public-securities-initial-public-offering-ipo-twelve/', publicsecuritiesinitialpublicofferingipotwelve, name='Public Securities - Initial Public Offering (IPO)twelve'),
    #path('public-securities-otc-over-the-counter/', publicsecuritiesotcoverthecounter, name='Public Securities - OTC Over the Counter'),
    #path('public-securities-otc-over-the-counter-faq/', publicsecuritiesotcoverthecounterfaq, name='Public Securities - OTC Over the Counterfaq'),
    #path('public-securities-otc-over-the-counter-twelve/', publicsecuritiesotcoverthecountertwelve, name='Public Securities - OTC Over the Countertwelve'),
    #path('venture-capital-mergers-and-acquisitions-financing/', venturecapitalmergersacquisitionsfinancing, name='Venture Capital - Mergers & Acquisitions Financing'),
    #path('venture-capital-mergers-and-acquisitions-financing-faq/', venturecapitalmergersacquisitionsfinancingfaq, name='Venture Capital - Mergers & Acquisitions Financingfaq'),
    #path('venture-capital-mergers-and-acquisitions-financing-twelve/', venturecapitalmergersacquisitionsfinancingtwelve, name='Venture Capital - Mergers & Acquisitions Financingtwelve'),
    #path('venture-capital-equity-sale/', venturecapitalequitysale, name='Venture Capital - Equity Sale'),
    #path('venture-capital-equity-sale-faq/', venturecapitalequitysalefaq, name='Venture Capital - Equity Salefaq'),
    #path('venture-capital-equity-sale-twelve/', venturecapitalequitysaletwelve, name='Venture Capital - Equity Saletwelve'),
]#
