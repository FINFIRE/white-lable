from django.urls import path
from .views import Match,summary,definition,faq,twelvevariable,pdf,word
from .capitalinformation.accelerator import accelerator,acceleratorfaq,acceleratortwelve
from .capitalinformation.acceleratorprivate1 import acceleratorprivate,acceleratorprivatefaq,acceleratorprivatetwelve
from .capitalinformation.acceleratorpublic2 import acceleratorpublic,acceleratorpublicfaq,acceleratorpublictwelve
from .capitalinformation.acceleratoruniversity3 import acceleratoruniversity,acceleratoruniversityfaq,acceleratoruniversitytwelve
from .capitalinformation.appscabbage4 import appscabbage,appscabbagefaq,appscabbagetwelve
from .capitalinformation.bonds import bonds,bondsfaq,bondstwelve
from .capitalinformation.bondsforeign5 import bondsforeign,bondsforeignfaq,bondsforeigntwelve
from .capitalinformation.bondsgovernmentbacked6 import bondsgovernmentbacked,bondsgovernmentbackedfaq,bondsgovernmentbackedtwelve
from .capitalinformation.bondshighyieldjunk7 import bondshighyieldjunk,bondshighyieldjunkfaq,bondshighyieldjunktwelve
from .capitalinformation.bondsinvestmentgrade8 import bondsinvestmentgrade,bondsinvestmentgradefaq,bondsinvestmentgradetwelve
from .capitalinformation.bondsmortgagebacked9 import bondsmortgagebacked,bondsmortgagebackedfaq,bondsmortgagebackedtwelve
from .capitalinformation.bootstrappedcashsaving10 import bootstrappedcashsaving,bootstrappedcashsavingfaq,bootstrappedcashsavingtwelve
from .capitalinformation.bootstrappedhomeequity11 import bootstrappedhomeequity,bootstrappedhomeequityfaq,bootstrappedhomeequitytwelve
from .capitalinformation.bootstrappedpersonalcreditcards12 import bootstrappedpersonalcreditcards,bootstrappedpersonalcreditcardsfaq,bootstrappedpersonalcreditcardstwelve
from .capitalinformation.bootstrappedretirement401ksdi13 import bootstrappedretirement401ksdi,bootstrappedretirement401ksdifaq,bootstrappedretirement401ksditwelve
from .capitalinformation.bootstrappedwholelifeinsurance14 import bootstrappedwholelifeinsurance,bootstrappedwholelifeinsurancefaq,bootstrappedwholelifeinsurancetwelve
from .capitalinformation.bootstrapped import bootstrapped,bootstrappedfaq,bootstrappedtwelve
from .capitalinformation.commercialbanking import commercialbanking,commercialbankingfaq,commercialbankingtwelve
from .capitalinformation.commercialbankingacquisitionloan15 import commercialbankingacquisitionloan,commercialbankingacquisitionloanfaq,commercialbankingacquisitionloantwelve
from .capitalinformation.commercialbankingassestbased16 import commercialbankingassestbased,commercialbankingassestbasedfaq,commercialbankingassestbasedtwelve
from .capitalinformation.commercialbankingcollateralizeddebt17 import commercialbankingcollateralizeddebt,commercialbankingcollateralizeddebtfaq,commercialbankingcollateralizeddebttwelve
from .capitalinformation.commercialbankingcommercialbankloan18 import commercialbankingcommercialbankloan,commercialbankingcommercialbankloanfaq,commercialbankingcommercialbankloantwelve
from .capitalinformation.commercialbankingcreditcard19 import commercialbankingcreditcard,commercialbankingcreditcardfaq,commercialbankingcreditcardtwelve
from .capitalinformation.commercialbankingequipmentloan20 import commercialbankingequipmentloan,commercialbankingequipmentloanfaq,commercialbankingequipmentloantwelve
from .capitalinformation.commercialbankinglineofcredit21 import commercialbankinglineofcredit,commercialbankinglineofcreditfaq,commercialbankinglineofcredittwelve
from .capitalinformation.commercialbankingrealestateloan22 import commercialbankingrealestateloan,commercialbankingrealestateloanfaq,commercialbankingrealestateloantwelve
from .capitalinformation.commercialbankingstandbylinesofcredit23 import commercialbankingstandbylinesofcredit,commercialbankingstandbylinesofcreditfaq,commercialbankingstandbylinesofcredittwelve
from .capitalinformation.cryptocurrency import cryptocurrency,cryptocurrencyfaq,cryptocurrencytwelve
from .capitalinformation.cryptocurrencyinitialcoinoffering24 import cryptocurrencyinitialcoinoffering,cryptocurrencyinitialcoinofferingfaq,cryptocurrencyinitialcoinofferingtwelve
from .capitalinformation.cryptocurrencyinitialexchangeoffering25 import cryptocurrencyinitialexchangeoffering,cryptocurrencyinitialexchangeofferingfaq,cryptocurrencyinitialexchangeofferingtwelve
from .capitalinformation.cryptocurrencyinvestmentviacryptowallet26 import cryptocurrencyinvestmentviacryptowallet,cryptocurrencyinvestmentviacryptowalletfaq,cryptocurrencyinvestmentviacryptowallettwelve
from .capitalinformation.factoring import factoring,factoringfaq,factoringtwelve
from .capitalinformation.factoringaccountsreceivable27 import factoringaccountsreceivable,factoringaccountsreceivablefaq,factoringaccountsreceivabletwelve
from .capitalinformation.factoringinvoicefactoring28 import factoringinvoicefactoring,factoringinvoicefactoringfaq,factoringinvoicefactoringtwelve
from .capitalinformation.factoringmerchantaccountadvances29 import factoringmerchantaccountadvances,factoringmerchantaccountadvancesfaq,factoringmerchantaccountadvancestwelve
from .capitalinformation.factoringpurchaseorderloan30 import factoringpurchaseorderloan,factoringpurchaseorderloanfaq,factoringpurchaseorderloantwelve
from .capitalinformation.governmentincentiveeb5immigration31 import governmentincentiveeb5immigration,governmentincentiveeb5immigrationfaq,governmentincentiveeb5immigrationtwelve
from .capitalinformation.governmentincentiveenterprisezone32 import governmentincentiveenterprisezone,governmentincentiveenterprisezonefaq,governmentincentiveenterprisezonetwelve
from .capitalinformation.governmentincentives import governmentincentives,governmentincentivesfaq,governmentincentivestwelve
from .capitalinformation.grants import grants,grantsfaq,grantstwelve
from .capitalinformation.grantscorporategrants33 import grantscorporategrants,grantscorporategrantsfaq,grantscorporategrantstwelve
from .capitalinformation.grantseducationgrants34 import grantseducationgrants,grantseducationgrantsfaq,grantseducationgrantstwelve
from .capitalinformation.grantsgovernment35 import grantsgovernment,grantsgovernmentfaq,grantsgovernmenttwelve
from .capitalinformation.grantsmunicipalities36 import grantsmunicipalities,grantsmunicipalitiesfaq,grantsmunicipalitiestwelve
from .capitalinformation.grantsresearchgrants37 import grantsresearchgrants,grantsresearchgrantsfaq,grantsresearchgrantstwelve
from .capitalinformation.grantsstateagencies38 import grantsstateagencies,grantsstateagenciesfaq,grantsstateagenciestwelve
from .capitalinformation.hedgefunds import hedgefunds,hedgefundsfaq,hedgefundstwelve
from .capitalinformation.hedgefundsprivate39 import hedgefundsprivate,hedgefundsprivatefaq,hedgefundsprivatetwelve
from .capitalinformation.hedgefundspublic40 import hedgefundspublic,hedgefundspublicfaq,hedgefundspublictwelve
from .capitalinformation.incubator import incubator,incubatorfaq,incubatortwelve
from .capitalinformation.incubatorprivate41 import incubatorprivate,incubatorprivatefaq,incubatorprivatetwelve
from .capitalinformation.incubatorpublic42 import incubatorpublic,incubatorpublicfaq,incubatorpublictwelve
from .capitalinformation.incubatoruniversity43 import incubatoruniversity,incubatoruniversityfaq,incubatoruniversitytwelve
from .capitalinformation.investmentbanking import investmentbanking,investmentbankingfaq,investmentbankingtwelve
from .capitalinformation.investmentbankingbrokerdealerrepresentation44 import investmentbankingbrokerdealerrepresentation,investmentbankingbrokerdealerrepresentationfaq,investmentbankingbrokerdealerrepresentationtwelve
from .capitalinformation.investmentbankingbrokersyndication45 import investmentbankingbrokersyndication,investmentbankingbrokersyndicationfaq,investmentbankingbrokersyndicationtwelve
from .capitalinformation.investmentbankingequitysales46 import investmentbankingequitysales,investmentbankingequitysalesfaq,investmentbankingequitysalestwelve
from .capitalinformation.investmentbankinginvestmentbankerdebt47 import investmentbankinginvestmentbankerdebt,investmentbankinginvestmentbankerdebtfaq,investmentbankinginvestmentbankerdebttwelve
from .capitalinformation.investmentbankingmezzaninefinancing48 import investmentbankingmezzaninefinancing,investmentbankingmezzaninefinancingfaq,investmentbankingmezzaninefinancingtwelve
from .capitalinformation.privatedebt import privatedebt,privatedebtfaq,privatedebttwelve
from .capitalinformation.privatedebtacquisitionloan49 import privatedebtacquisitionloan,privatedebtacquisitionloanfaq,privatedebtacquisitionloantwelve
from .capitalinformation.privatedebtassetbasedlending50 import privatedebtassetbasedlending,privatedebtassetbasedlendingfaq,privatedebtassetbasedlendingtwelve
from .capitalinformation.privatedebtbridgefinancing51 import privatedebtbridgefinancing,privatedebtbridgefinancingfaq,privatedebtbridgefinancingtwelve
from .capitalinformation.privatedebtcollaterizeddebt52 import privatedebtcollaterizeddebt,privatedebtcollaterizeddebtfaq,privatedebtcollaterizeddebttwelve
from .capitalinformation.privatedebthardmoneyloan53 import privatedebthardmoneyloan,privatedebthardmoneyloanfaq,privatedebthardmoneyloantwelve
from .capitalinformation.privatedebtprivatedebt54 import privatedebtprivatedebt,privatedebtprivatedebtfaq,privatedebtprivatedebttwelve
from .capitalinformation.privatedebtpromisorynote55 import privatedebtpromisorynote,privatedebtpromisorynotefaq,privatedebtpromisorynotetwelve
from .capitalinformation.privatedebtrealestateloan56 import privatedebtrealestateloan,privatedebtrealestateloanfaq,privatedebtrealestateloantwelve
from .capitalinformation.privateequitysecurities import privateequitysecurities,privateequitysecuritiesfaq,privateequitysecuritiestwelve
from .capitalinformation.privateequitysecuritiesacrreditedinvestors57 import privateequitysecuritiesacrreditedinvestors,privateequitysecuritiesacrreditedinvestorsfaq,privateequitysecuritiesacrreditedinvestorstwelve
from .capitalinformation.privateequitysecuritiesangelinvestors58 import privateequitysecuritiesangelinvestors,privateequitysecuritiesangelinvestorsfaq,privateequitysecuritiesangelinvestorstwelve
from .capitalinformation.privateequitysecuritiesbrokerdealers3378_59 import privateequitysecuritiesbrokerdealers3378_,privateequitysecuritiesbrokerdealers3378_faq,privateequitysecuritiesbrokerdealers3378_twelve
from .capitalinformation.privateequitysecuritiesconvertiblenote60 import privateequitysecuritiesconvertiblenote,privateequitysecuritiesconvertiblenotefaq,privateequitysecuritiesconvertiblenotetwelve
from .capitalinformation.privateequitysecuritiesfamilyandfriends61 import privateequitysecuritiesfamilyandfriends,privateequitysecuritiesfamilyandfriendsfaq,privateequitysecuritiesfamilyandfriendstwelve
from .capitalinformation.privateequitysecuritiesfamilyoffices62 import privateequitysecuritiesfamilyoffices,privateequitysecuritiesfamilyofficesfaq,privateequitysecuritiesfamilyofficestwelve
from .capitalinformation.privateequitysecuritieshighnetworthindividuals63 import privateequitysecuritieshighnetworthindividuals,privateequitysecuritieshighnetworthindividualsfaq,privateequitysecuritieshighnetworthindividualstwelve
from .capitalinformation.privateequitysecuritiesprivateplacementmemorandum64 import privateequitysecuritiesprivateplacementmemorandum,privateequitysecuritiesprivateplacementmemorandumfaq,privateequitysecuritiesprivateplacementmemorandumtwelve
from .capitalinformation.privateequitysecuritiesregulationa65 import privateequitysecuritiesregulationa,privateequitysecuritiesregulationafaq,privateequitysecuritiesregulationatwelve
from .capitalinformation.privateequitysecuritiesregulationCFtitleIII66 import privateequitysecuritiesregulationCFtitleIII,privateequitysecuritiesregulationCFtitleIIIfaq,privateequitysecuritiesregulationCFtitleIIItwelve
from .capitalinformation.privateequitysecuritiesregulationd504_67 import privateequitysecuritiesregulationd504_,privateequitysecuritiesregulationd504_faq,privateequitysecuritiesregulationd504_twelve
from .capitalinformation.privateequitysecuritiesregulationd506b68 import privateequitysecuritiesregulationd506b,privateequitysecuritiesregulationd506bfaq,privateequitysecuritiesregulationd506btwelve
from .capitalinformation.privateequitysecuritiesregulationd506c69 import privateequitysecuritiesregulationd506c,privateequitysecuritiesregulationd506cfaq,privateequitysecuritiesregulationd506ctwelve
from .capitalinformation.privateequitysecuritiesrule144_70 import privateequitysecuritiesrule144_,privateequitysecuritiesrule144_faq,privateequitysecuritiesrule144_twelve
from .capitalinformation.privateequitysecuritiessimpleagreementfutureequity71 import privateequitysecuritiessimpleagreementfutureequity,privateequitysecuritiessimpleagreementfutureequityfaq,privateequitysecuritiessimpleagreementfutureequitytwelve
from .capitalinformation.royaltyfinancing import royaltyfinancing,royaltyfinancingfaq,royaltyfinancingtwelve
from .capitalinformation.royaltyfinancingtoplinerevenue72 import royaltyfinancingtoplinerevenue,royaltyfinancingtoplinerevenuefaq,royaltyfinancingtoplinerevenuetwelve
from .capitalinformation.SmallBusinessAdministration import SmallBusinessAdministration,SmallBusinessAdministrationfaq,SmallBusinessAdministrationtwelve
from .capitalinformation.smallbusinessadministration504B73 import smallbusinessadministration504B,smallbusinessadministration504Bfaq,smallbusinessadministration504Btwelve
from .capitalinformation.smallbusinessadministration7a74 import smallbusinessadministration7a,smallbusinessadministration7afaq,smallbusinessadministration7atwelve
from .capitalinformation.smallbusinessadministrationcdcsbdc77 import smallbusinessadministrationcdcsbdc,smallbusinessadministrationcdcsbdcfaq,smallbusinessadministrationcdcsbdctwelve
from .capitalinformation.smallbusinessadministrationexpress75 import smallbusinessadministrationexpress,smallbusinessadministrationexpressfaq,smallbusinessadministrationexpresstwelve
from .capitalinformation.smallbusinessadministrationsbic78 import smallbusinessadministrationsbic,smallbusinessadministrationsbicfaq,smallbusinessadministrationsbictwelve
from .capitalinformation.smallbusinessadministrationveteran76 import smallbusinessadministrationveteran,smallbusinessadministrationveteranfaq,smallbusinessadministrationveterantwelve
from .capitalinformation.thirdpartycorporatecredit79 import thirdpartycorporatecredit,thirdpartycorporatecreditfaq,thirdpartycorporatecredittwelve
from .capitalinformation.tokenization80 import tokenization,tokenizationfaq,tokenizationtwelve
from .capitalinformation.venturecapital import venturecapital,venturecapitalfaq,venturecapitaltwelve
from .capitalinformation.venturecapitalequitysale81 import venturecapitalequitysale,venturecapitalequitysalefaq,venturecapitalequitysaletwelve
from .capitalinformation.venturecapitallongtermdebt82 import venturecapitallongtermdebt,venturecapitallongtermdebtfaq,venturecapitallongtermdebttwelve
from .capitalinformation.venturecapitalmezzaninefinancing83 import venturecapitalmezzaninefinancing,venturecapitalmezzaninefinancingfaq,venturecapitalmezzaninefinancingtwelve


urlpatterns = [
    path('match/', Match, name='match'),
    path('word/',word,name='word'),
    path('pdf/',pdf,name='pdf'),
    path('definitions/',definition,name='definition'),
    path('twelvevairable/',twelvevariable,name='twelvevariable'),
    path('FAQ/',faq, name='FAQ'),
    path('summary-of-response/',summary,name='summary-of-response'),
    #path('acceleratoruniversity/',acceleratoru,name ='Accelerator University'),
    #path('acceleratoruniversityfaq/',acceleratorufaq,name='Accelerator Universityfaq'),
    #path('acceleratoruniversitytwelve/',acceleratorutwelve,name='Accelerator Universitytwelve'),
    #path('appscabbage/',appscabbage,name ='Apps (i.e. Cabbage)'),
    #path('appscabbagefaq/',appscabbagefaq,name='Apps (i.e. Cabbage)faq'),
    #path('appscabbagetwelve/',appscabbagetwelve,name='Apps (i.e. Cabbage)twelve'),
    path('grants/',grants,name ='Grants'),
    path('grants-faq/',grantsfaq,name='Grantsfaq'),
    path('grants-twelve/',grantstwelve,name='Grantstwelve'),    
    path('bonds/',bonds,name ='Bonds'),
    path('bonds-faq/',bondsfaq,name='Bondsfaq'),
    path('bonds-twelve/',bondstwelve,name='Bondstwelve'), 
    path('bootstrapped/',bootstrapped,name ='Bootstrapped'),
    path('bootstrapped-faq/',bootstrappedfaq,name='Bootstrappedfaq'),
    path('bootstrapped-twelve/',bootstrappedtwelve,name='Bootstrappedtwelve'),         
    #path('governmentincentiveeb/',governmentincentiveeb5,name ='Government Incentives - EB5 Immigration'),
    #path('governmentincentiveebfaq/',governmentincentiveeb5faq,name='Government Incentives - EB5 Immigrationfaq'),
    #path('governmentincentiveebtwelve/',governmentincentiveeb5twelve,name='Government Incentives - EB5 Immigrationtwelve'),
    path('governmentincentives/',governmentincentives,name ='Government Incentives'),
    path('governmentincentivesfaq/',governmentincentivesfaq,name='Government Incentivesfaq'),
    path('governmentincentivestwelve/',governmentincentivestwelve,name='Government Incentivestwelve'),    
    path('incubator-private/',incubatorprivate,name ='Incubator'),
    path('incubator-private-faq/',incubatorprivatefaq,name='Incubatorfaq'),
    path('incubator-private-twelve/',incubatorprivatetwelve,name='Incubatortwelve'),
    path('incubator/',incubator,name ='Incubator'),
    path('incubator-faq/',incubatorfaq,name='Incubatorfaq'),
    path('incubator-twelve/',incubatortwelve,name='Incubatortwelve'),    
    #path('incubatorpublic/',incubatorpublic,name ='Incubator - Public'),
    #path('incubatorpublicfaq/',incubatorpublicfaq,name='Incubator - Publicfaq'),
    #path('incubatorpublictwelve/',incubatorpublictwelve,name='Incubator - Publictwelve'),
    #path('incubatoruniversity/',incubatoruniversity,name ='Incubator - University'),
    #path('incubatoruniversityfaq/',incubatoruniversityfaq,name='Incubator - Universityfaq'),
    #path('incubatoruniversitytwelve/',incubatoruniversitytwelve,name='Incubator - Universitytwelve'),
    #path('investment-banking-broker-dealer/',investmentbankingbrokerdealerrepresentation,name ='Investment Banking'),
    #path('investment-banking-broker-dealer-faq/',investmentbankingbrokerdealerrepresentationfaq,name='Investment Bankingfaq'),
    #path('investment-banking-broker-dealer-twelve/',investmentbankingbrokerdealerrepresentationtwelve,name='Investment Bankingtwelve'),
    path('investment-banking/',investmentbanking,name ='Investment Banking'),
    path('investment-banking-faq/',investmentbankingfaq,name='Investment Bankingfaq'),
    path('investment-banking-twelve/',investmentbankingtwelve,name='Investment Bankingtwelve'),    
    #path('convertiblenote/',convertiblenote,name ='Private Equity Securities - Convertible Note'),
    #path('convertiblenotefaq/',convertiblenotefaq,name='Private Equity Securities - Convertible Notefaq'),
    #path('convertiblenotetwelve/',convertiblenotetwelve,name='Private Equity Securities - Convertible Notetwelve'),
    path('private-equity-securities/',privateequitysecurities,name ='Private Equity Securities'),
    path('private-equity-securities-faq/',privateequitysecuritiesfaq,name='Private Equity Securitiesfaq'),
    path('private-equity-securities-twelve/',privateequitysecuritiestwelve,name='Private Equity Securitiestwelve'),    
    #path('cryptoinitialcoinoffering/',cryptoinitialcoinoffering,name ='Cryptocurrency - Initial Coin Offering'),
    #path('cryptoinitialcoinofferingfaq/',cryptoinitialcoinofferingfaq,name='Cryptocurrency - Initial Coin Offeringfaq'),
    #path('cryptoinitialcoinofferingtwelve/',cryptoinitialcoinofferingtwelve,name='Cryptocurrency - Initial Coin Offeringtwelve'),
    #path('cryptoinitialexchangeffering/',cryptoinitialexchangeoffering,name ='Cryptocurrency - Initial Exchange Offering'),
    #path('cryptoinitialexchangeofferingfaq/',cryptoinitialexchangeofferingfaq,name='Cryptocurrency - Initial Exchange Offeringfaq'),
    #path('cryptoinitialexchangeofferingtwelve/',cryptoinitialexchangeofferingtwelve,name='Cryptocurrency - Initial Exchange Offeringtwelve'),    
    #path('crypto-investment-via-wallet/',cryptowallet,name ='Cryptocurrency'),
    #path('crypto-investment-via-wallet-faq/',cryptowalletfaq,name='Cryptocurrencyfaq'),
    #path('crypto-investment-via-wallet-twelve/',cryptowallettwelve,name='Cryptocurrencytwelve'),
    path('crypto-currency/',cryptocurrency,name ='Cryptocurrency'),
    path('crypto-currency-faq/',cryptocurrencyfaq,name='Cryptocurrencyfaq'),
    path('crypto-currency-twelve/',cryptocurrencytwelve,name='Cryptocurrencytwelve'),    
    path('accelerator-private/',accelerator,name ='Accelerator'),
    path('accelerator-private-faq/',acceleratorfaq,name='Acceleratorfaq'),
    path('accelerator-private-twelve/',acceleratortwelve,name='Acceleratortwelve'),
    #path('acceleratorpublic/',acceleratorpublic,name ='Accelerator - Public'),
    #path('acceleratorpublicfaq/',acceleratorpublicfaq,name='Accelerator - Publicfaq'),
    #path('acceleratorpublictwelve/',acceleratorpublictwelve,name='Accelerator - Publictwelve'),
    #path('sbaveteran/',sbaveteran,name ='Small Business Administration (SBA) - SBA Veteran'),
    #path('sbaveteranfaq/',sbaveteranfaq,name='Small Business Administration (SBA) - SBA Veteranfaq'),
    #path('sbaveterantwelve/',sbaveterantwelve,name='Small Business Administration (SBA) - SBA Veterantwelve'),    
    #path('commercialbankloan/',commercialbankloan,name ='Commercial Banking - Commercial Bank Loan (4,135)'),
    #path('commercialbankloanfaq/',commercialbankloanfaq,name='Commercial Banking - Commercial Bank Loan (4,135)faq'),
    #path('commercialbankloantwelve/',commercialbankloantwelve,name='Commercial Banking - Commercial Bank Loan (4,135)twelve'),
    #path('commercialbankingacqusition/',commercialbankacquisition,name ='Commercial Banking - Acquisition Loan'),
    #path('commercialbankingacqusitionfaq/',commercialbankacquisitionfaq,name='Commercial Banking - Acquisition Loanfaq'),
    #path('commercialbankingacqusitiontwelve/',commercialbankacquisitiontwelve,name='Commercial Banking - Acquisition Loantwelve'),
    #path('commercialbankassestbased/',commercialbankassestbased,name ='Commercial Banking - Asset Based Lending'),
    #path('commercialbankassestbasedfaq/',commercialbankassestbasedfaq,name='Commercial Banking - Asset Based Lendingfaq'),
    #path('commercialbankassestbasedtwelve/',commercialbankassestbasedtwelve,name='Commercial Banking - Asset Based Lendingtwelve'),
    #path('commercialbankcollateralizeddebt/',commercialbankcollateralizeddebt,name ='Commercial Banking - Collateralized Debt'),
    #path('commercialbankcollateralizeddebtfaq/',commercialbankcollateralizeddebtfaq,name='Commercial Banking - Collateralized Debtfaq'),
    #path('commercialbankcollateralizeddebttwelve/',commercialbankcollateralizeddebttwelve,name='Commercial Banking - Collateralized Debttwelve'),
    #path('commercial-bank-loan/',commercialbankequipmentloan,name ='Commercial Banking'),
    #path('commercial-bank-loan-faq/',commercialbankequipmentloanfaq,name='Commercial Bankingfaq'),
    #path('commercial-bank-loan-twelve/',commercialbankequipmentloantwelve,name='Commercial Bankingtwelve'),
    path('commercial-bank-loan/',commercialbanking,name ='Commercial Banking'),
    path('commercial-bank-loan-faq/',commercialbankingfaq,name='Commercial Bankingfaq'),
    path('commercial-bank-loan-twelve/',commercialbankingtwelve,name='Commercial Bankingtwelve'),    
    #path('commercialbankrealestate/',commercialbankrealestate,name ='Commercial Banking - Real Estate Loan'),
    #path('commercialbankrealestatefaq/',commercialbankrealestatefaq,name='Commercial Banking - Real Estate Loanfaq'),
    #path('commercialbankrealestatetwelve/',commercialbankrealestatetwelve,name='Commercial Banking - Real Estate Loantwelve'),
    #path('commercialbankstandbylinesofcredit/',commercialbankstandbylinesofcredit,name ='Commercial Banking - Standby Lines of Credit'),
    #path('commercialbankstandbylinesofcreditfaq/',commercialbankstandbylinesofcreditfaq,name='Commercial Banking - Standby Lines of Creditfaq'),
    #path('commercialbankstandbylinesofcredittwelve/',commercialbankstandbylinesofcredittwelve,name='Commercial Banking - Standby Lines of Credittwelve'),
    path('creditcard/',commercialbankingcreditcard,name ='Commercial Banking - Credit Card'),
    path('creditcardfaq/',commercialbankingcreditcardfaq,name='Commercial Banking - Credit Cardfaq'),
    path('creditcardtwelve/',commercialbankingcreditcardtwelve,name='Commercial Banking - Credit Cardtwelve'),
    path('factoring-accounts-recievables/',factoringaccountsreceivable,name ='Factoring'),
    path('factoring-accounts-recievables-faq/',factoringaccountsreceivablefaq,name='Factoringfaq'),
    path('factoring-accounts-recievables-twelve/',factoringaccountsreceivabletwelve,name='Factoringtwelve'),
    path('factoring/',factoring,name ='Factoring'),
    path('factoring-faq/',factoringfaq,name='Factoringfaq'),
    path('factoring-twelve/',factoringtwelve,name='Factoringtwelve'),    
    #path('hedge-funds-private/',hedgefundsprivate,name ='Hedge Funds'),
    #path('hedge-funds-private-faq/',hedgefundsprivatefaq,name='Hedge Fundsfaq'),
    #path('hedge-funds-private-twelve/',hedgefundsprivatetwelve,name='Hedge Fundstwelve'),
    path('hedge-funds/',hedgefunds,name ='Hedge Funds'),
    path('hedge-funds-faq/',hedgefundsfaq,name='Hedge Fundsfaq'),
    path('hedge-funds-twelve/',hedgefundstwelve,name='Hedge Fundstwelve'),    
    #path('hedgefundspublic/',hedgefundspublic,name ='Hedge Funds - Public'),
    #path('hedgefundspublicfaq/',hedgefundspublicfaq,name='Hedge Funds - Publicfaq'),
    #path('hedgefundspublictwelve/',hedgefundspublictwelve,name='Hedge Funds - Publictwelve'),
    #path('private-bridge-financing/',privatebridgefinancing,name ='Private Debt'),
    #path('private-bridge-financing-faq/',privatebridgefinancingfaq,name='Private Debtfaq'),
    #path('private-bridge-financing-twelve/',privatebridgefinancingtwelve,name='Private Debttwelve'),
    path('private-debt/',privatedebt,name ='Private Debt'),
    path('private-debt-faq/',privatedebtfaq,name='Private Debtfaq'),
    path('private-debt-twelve/',privatedebttwelve,name='Private Debttwelve'),    
    #path('privatedebtprivatedebt/',privatedebtprivatedebt,name ='Private Debt - Private Debt'),
    #path('privatedebtprivatedebtfaq/',privatedebtprivatedebtfaq,name='Private Debt - Private Debtfaq'),
    #path('privatedebtprivatedebttwelve/',privatedebtprivatedebttwelve,name='Private Debt - Private Debttwelve'),
    #path('privatedebtpromisorynote/',privatepromisorynote,name ='Private Debt - Promissory Note'),
    #path('privatedebtpromisorynotefaq/',privatepromisorynotefaq,name='Private Debt - Promissory Notefaq'),
    #path('privatedebtpromisorynotetwelve/',privatepromisorynotetwelve,name='Private Debt - Promissory Notetwelve'),
    #path('regulationd504/',regulationd504,name ='Private Equity Securities - Regulation D 504'),
    #path('regulationd504faq/',regulationd504faq,name='Private Equity Securities - Regulation D 504faq'),
    #path('regulationd504twelve/',regulationd504twelve,name='Private Equity Securities - Regulation D 504twelve'),
    #path('regulationd506b/',regulationd506b,name ='Private Equity Securities - Regulation D 506(b)'),
    #path('regulationd506bfaq/',regulationd506bfaq,name='Private Equity Securities - Regulation D 506(b)faq'),
    #path('regulationd506btwelve/',regulationd506btwelve,name='Private Equity Securities - Regulation D 506(b)twelve'),
    #path('regulationd506c/',regulationd506c,name ='Private Equity Securities - Regulation D 506(c)'),
    #path('regulationd506cfaq/',regulationd506cfaq,name='Private Equity Securities - Regulation D 506(c)faq'),
    #path('regulationd506ctwelve/',regulationd506ctwelve,name='Private Equity Securities - Regulation D 506(c)twelve'),        
    #path('regulation-crowd-funding/',regulation_crowdfunding, name='Private Equity Securities'),
    #path('regulation-crowd-funding-faq/', regulation_crowdfundingfaq, name='Private Equity Securitiesfaq'),
    #path('regulation-crowd-funding-twelve/', regulation_crowdfundingtwelve, name='Private Equity Securitiestwelve'),
    #path('royalty-financing/',royaltyfinancing, name='Royalty Financing'),
    #path('royalty-financing-faq/', royaltyfinancingfaq, name='Royalty Financingfaq'),
    #path('royalty-financing-twelve/', royaltyfinancingtwelve, name='Royalty Financingtwelve'),
    path('royalty-financing/',royaltyfinancing, name='Royalty Financing'),
    path('royalty-financing-faq/', royaltyfinancingfaq, name='Royalty Financingfaq'),
    path('royalty-financing-twelve/', royaltyfinancingtwelve, name='Royalty Financingtwelve'),    
    path('third-party-corporate-credit/',thirdpartycorporatecredit, name='Third Party Corporate Credit'),
    path('third-party-corporate-credit-faq/', thirdpartycorporatecreditfaq, name='Third Party Corporate Creditfaq'),
    path('third-party-corporate-credit-twelve/', thirdpartycorporatecredittwelve, name='Third Party Corporate Credittwelve'),
    #path('rule144/',rule144, name='Private Equity Securities - Rule 144'),
    #path('rule144faq/', rule144faq, name='Private Equity Securities - Rule 144faq'),
    #path('rule144twelve/', rule144twelve, name='Private Equity Securities - Rule 144twelve'),
    #path('sba504/', sba504b, name='Small Business Administration (SBA) - SBA 504B'),
    #path('sba504faq/', sba504bfaq, name='Small Business Administration (SBA) - SBA 504Bfaq'),
    #path('sba504twelve/', sba504btwelve, name='Small Business Administration (SBA) - SBA 504Btwelve'),
    #path('sba-7a/', sba7a, name='Small Business Administration (SBA)'),
    #path('sba-7a-faq/', sba7afaq, name='Small Business Administration (SBA)faq'),
    #path('sba-7a-twelve/', sba7atwelve, name='Small Business Administration (SBA)twelve'),
    path('small-business-administration/', SmallBusinessAdministration, name='Small Business Administration (SBA)'),
    path('small-business-administration-faq/', SmallBusinessAdministrationfaq, name='Small Business Administration (SBA)faq'),
    path('small-business-administration-twelve/', SmallBusinessAdministrationtwelve, name='Small Business Administration (SBA)twelve'),    
    #path('sbadbdc/', sbasbdc, name='Small Business Administration (SBA) - CDC/SBDC'),
    #path('sbadbdcfaq/', sbasbdcfaq, name='Small Business Administration (SBA) - CDC/SBDCfaq'),
    #path('sbadbdctwelve/', sbasbdctwelve, name='Small Business Administration (SBA) - CDC/SBDCtwelve'),
    #path('sbasbic/', sbasbic, name='Small Business Administration (SBA) - SBIC'),
    #path('sbasbicfaq/', sbasbicfaq, name='Small Business Administration (SBA) - SBICfaq'),
    #path('sbasbictwelve/', sbasbictwelve, name='Small Business Administration (SBA) - SBICtwelve'),
    #path('sbaexpress/', sbaexpress, name='Small Business Administration (SBA) - SBA Express'),
    #path('sbaexpressfaq/', sbaexpressfaq, name='Small Business Administration (SBA) - SBA Expressfaq'),
    #path('sbaexpresstwelve/', sbaexpresstwelve, name='Small Business Administration (SBA) - SBA Expresstwelve'),
    #path('regulationa/', regulationa, name='Private Equity Securities - Regulation A'),
    #path('regulationafaq/', regulationafaq, name='Private Equity Securities - Regulation Afaq'),
    #path('regulationatwelve/', regulationatwelve, name='Private Equity Securities - Regulation Atwelve'),
    #path('safe/', safe, name='Private Equity Securities - Simple Agreement Future Equity'),
    #path('safefaq/', safefaq, name='Private Equity Securities - Simple Agreement Future Equityfaq'),
    #path('safetwelve/', safetwelve, name='Private Equity Securities - Simple Agreement Future Equitytwelve'),
    path('tokenization/', tokenization, name='Tokenization'),
    path('tokenizationfaq/', tokenizationfaq, name='Tokenizationfaq'),
    path('tokenizationtwelve/', tokenizationtwelve, name='Tokenizationtwelve'),
    path('linseofcredit/', commercialbankinglineofcredit, name='Commercial Banking - Line of Credit'),
    path('linseofcreditfaq/', commercialbankinglineofcreditfaq, name='Commercial Banking - Line of Creditfaq'),
    path('linseofcredittwelve/', commercialbankinglineofcredittwelve, name='Commercial Banking - Line of Credittwelve'),
    path('vcequitysales/', venturecapital, name='Venture Capital'),
    path('vcequitysalesfaq/', venturecapitalfaq, name='Venture Capitalfaq'),
    path('vcequitysalestwelve/', venturecapitaltwelve, name='Venture Capitaltwelve'),
    #path('vclongtermdebt/', vclongtermdebt, name='Venture Capital - Long Term Debt'),
    #path('vclongtermdebtfaq/', vclongtermdebtfaq, name='Venture Capital - Long Term Debtfaq'),
    #path('vclongtermdebttwelve/', vclongtermdebttwelve, name='Venture Capital - Long Term Debttwelve'),
    #path('vcmezzaninefinancing/', vcmezzaninefinancing, name='Venture Capital - Mezzanine Financing'),
    #path('vcmezzaninefinancingfaq/', vcmezzaninefinancingfaq, name='Venture Capital - Mezzanine Financingfaq'),
    #path('vcmezzaninefinancingtwelve/', vcmezzaninefinancingtwelve, name='Venture Capital - Mezzanine Financingtwelve'),
]