from django.shortcuts import render,HttpResponse,redirect
from django.utils.safestring import mark_safe
from entreprise_questions.models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,\
EQuestions6,EQuestions7,EQuestions8,EQuestions9,EQuestions10,EQuestions11,EQuestions12,EQuestions13,EQuestions14,DocumentsPrepared
from iquestions.models import IQuestions1,IQuestions2
from registration.models import User,UserDetail,UserDetail2
from connections.models import Match_Data
from datetime import datetime
from django.contrib.auth.decorators import login_required
from ..models import Capital_Matches,Matches_Purchased,Letter_Response,Purchases

def publicsecuritiesderivatives(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Public Securities</b></u><br>
    Capital Type: Derivatives </center></p>
    <p><b><u>Introduction</u></b><br>
    Public securities derivatives are financial instruments whose value is derived from an underlying asset such as stocks, bonds, commodities, interest rates, currencies, or market indexes, and are traded on regulated exchanges or over-the-counter markets. {n} fits that definition. Derivatives include options, futures, swaps, and other structured contracts that allow investors to hedge risk, speculate on price movements, or enhance portfolio returns. In the United States, derivatives markets are regulated by the U.S. Securities and Exchange Commission and the Commodity Futures Trading Commission depending on the type of instrument. Public derivatives play a critical role in capital markets by improving liquidity, enabling risk management, and supporting price discovery.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    1. Derivatives are contractual financial instruments whose value is based on the performance of an underlying asset. Common public derivatives include exchange-traded options, futures contracts, and standardized swaps. For example, equity options traded on exchanges derive value from publicly listed stocks, while futures contracts may track commodities or financial indexes. These instruments allow market participants to manage exposure to price volatility without directly owning the underlying asset (SEC, 2023).<br><br>
    2. Derivatives are best suited for institutional investors, hedge funds, portfolio managers, corporations hedging operational risk, and sophisticated individual investors. Corporations often use derivatives to hedge interest rate risk, currency exposure, or commodity price fluctuations. Investment managers use derivatives to enhance returns or protect against downside risk. Due to leverage and complexity, derivatives are generally unsuitable for inexperienced investors without proper risk understanding.<br><br>
    3. The derivatives regulatory framework in the United States evolved significantly after the 2008 financial crisis. The Dodd-Frank Wall Street Reform and Consumer Protection Act introduced enhanced oversight of swap markets and required central clearing for many standardized derivatives. The Commodity Futures Trading Commission regulates futures and swaps markets, while the SEC regulates security-based swaps and options. These reforms increased transparency, reduced systemic risk, and strengthened market integrity.<br><br>
    4. Derivatives involve significant financial risk due to leverage, counterparty exposure, and market volatility. Small price movements in the underlying asset can result in disproportionate gains or losses. Over-the-counter derivatives carry counterparty default risk unless centrally cleared. Additionally, derivatives may expose investors to liquidity risk and complex valuation challenges. Regulatory compliance, margin requirements, and reporting obligations further increase operational complexity.<br><br>
    5. Participation in public derivatives markets requires opening brokerage accounts approved for derivatives trading and meeting margin requirements. Institutional participants must implement internal risk management frameworks and comply with regulatory reporting standards. Successful use of derivatives depends on disciplined risk assessment, hedging strategy alignment, understanding of contract specifications, and continuous monitoring of market conditions.
    </p>
    <p><u><b>References</u></b><br>
    1. U.S. Securities and Exchange Commission. (2023). Investor Bulletin: An Introduction to Options. https://www.sec.gov/oiea/investor-alerts-bulletins/ib_introductionoptions<br>
    2. Commodity Futures Trading Commission. (n.d.). Futures & Options Markets Overview. https://www.cftc.gov/LearnAndProtect<br>
    3. Dodd-Frank Wall Street Reform and Consumer Protection Act. (2010). U.S. Congress. https://www.congress.gov/111/plaws/publ203/PLAW-111publ203.pdf<br>
    4. Options Clearing Corporation. (n.d.). Characteristics and Risks of Standardized Options. https://www.theocc.com/Company-Information/Documents-and-Archives/Options-Disclosure-Document<br>
    5. Investopedia. (n.d.). Derivatives Definition. https://www.investopedia.com/terms/d/derivative.asp
    </p>
    <p><b><u>Legal Qualification Requirements</b></u><br>
    • Brokerage Account Approved for Derivatives Trading<br>
    • Compliance with SEC and/or CFTC Regulations<br>
    • Margin Account Setup (if applicable)<br>
    • Risk Disclosure Acknowledgment<br>
    • Clearinghouse Participation (for standardized contracts)<br>
    • AML/KYC Compliance<br>
    • Reporting Compliance (for institutional participants)
    </p>
    <p><b><u>Supporting Document List</b></u><br>
    • Brokerage Account Agreement<br>
    • Options or Futures Trading Approval Forms<br>
    • Risk Disclosure Statement (e.g., Options Disclosure Document)<br>
    • Margin Agreement<br>
    • Clearing Agreement (if applicable)<br>
    • Institutional Risk Management Policy<br>
    • Regulatory Reporting Documentation<br>
    • Derivatives Trading Policy (for corporations)
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction}
    return render(request,'detail.html',context)

def publicsecuritiesderivativesfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Public Securities<br>
    Derivatives</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What are derivatives in public securities markets?</u></b><br>
    • Answer: Derivatives are financial contracts whose value is derived from an underlying asset such as stocks, bonds, commodities, currencies, interest rates, or market indexes.
    </p>
    <p><u><b>2. What are common types of derivatives?</u></b><br>
    • Answer: Common derivatives include options, futures, forwards, and swaps.
    </p>
    <p><u><b>3. How do derivatives work?</u></b><br>
    • Answer: Derivatives derive their value from the performance of an underlying asset, allowing investors to hedge risk, speculate on price movements, or enhance returns.
    </p>
    <p><u><b>4. What is an option contract?</u></b><br>
    • Answer: An option gives the holder the right, but not the obligation, to buy or sell an underlying asset at a predetermined price within a specified time period.
    </p>
    <p><u><b>5. What is a futures contract?</u></b><br>
    • Answer: A futures contract obligates parties to buy or sell an underlying asset at a predetermined price on a specific future date.
    </p>
    <p><u><b>6. What are swaps?</u></b><br>
    • Answer: Swaps are agreements between parties to exchange cash flows or financial obligations, commonly involving interest rates or currencies.
    </p>
    <p><u><b>7. Why do investors use derivatives?</u></b><br>
    • Answer: Investors use derivatives for hedging risk, portfolio management, speculation, arbitrage, and income strategies.
    </p>
    <p><u><b>8. Are derivatives traded publicly?</u></b><br>
    • Answer: Many derivatives are traded on regulated exchanges, while others are traded over-the-counter (OTC) between private parties.
    </p>
    <p><u><b>9. What are the risks of derivatives?</u></b><br>
    • Answer: Risks include leverage risk, market volatility, counterparty risk, liquidity risk, and potential losses exceeding the initial investment.
    </p>
    <p><u><b>10. What is leverage in derivatives?</u></b><br>
    • Answer: Leverage allows investors to control large positions with relatively small capital, magnifying both gains and losses.
    </p>
    <p><u><b>11. Who regulates derivatives markets?</u></b><br>
    • Answer: In the United States, derivatives markets are regulated primarily by the Securities and Exchange Commission (SEC) and the Commodity Futures Trading Commission (CFTC).
    </p>
    <p><u><b>12. Can derivatives be used for hedging?</u></b><br>
    • Answer: Yes, derivatives are commonly used to hedge against price fluctuations, interest rate changes, or currency movements.
    </p>
    <p><u><b>13. Do derivatives involve ownership of the underlying asset?</u></b><br>
    • Answer: Not necessarily; many derivatives settle in cash without transferring ownership of the underlying asset.
    </p>
    <p><u><b>14. Are derivatives suitable for all investors?</u></b><br>
    • Answer: No, derivatives are complex instruments that may not be appropriate for inexperienced or risk-averse investors.
    </p>
    <p><u><b>15. When should derivatives be considered in a capital markets strategy?</u></b><br>
    • Answer: Derivatives should be considered when managing financial risk exposure, implementing advanced trading strategies, or protecting portfolio value.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def publicsecuritiesderivativestwelve(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    entity = EQuestions2.objects.get(user=request.user).Selected_Option
    stage = EQuestions1.objects.get(user=request.user).Selected_Option
    preraise = EQuestions3.objects.get(user=request.user).Selected_Option
    premarket = EQuestions4.objects.get(user=request.user).Selected_Options
    raisegoal = EQuestions5.objects.get(user=request.user).Selected_Option
    useoffund = EQuestions7.objects.get(user=request.user).Selected_Options
    enterprisecost = EQuestions8.objects.get(user=request.user).Selected_Option2
    tranch = EQuestions6.objects.get(user=request.user).Selected_Option
    rounds = EQuestions6.objects.get(user=request.user).Selected_Options
    upfrontcost = EQuestions.objects.get(user=request.user).Selected_Option
    upfronttime = EQuestions.objects.get(user=request.user).Selected_Option2
    introduction = """
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Public Securities</b></u><br>
    Capital Type: Derivatives</p></center>
    <p><b><u>1 – Stage of Development Assessment</b></u><br>
    Public derivatives are typically utilized by public companies, institutional investors, hedge funds, commodity producers, and financial institutions. Operating companies rarely use derivatives to raise capital directly; instead, derivatives are used for hedging, leverage, or structured financing strategies. {stage} is {{stage}} applicable.
    </p>
    <p><b><u>2 – Entity Type Assessment</b></u><br>
    Most appropriate for public corporations, registered investment funds, institutional trading entities, and large private companies with treasury operations. Entities must meet brokerage and clearing requirements. {{entity}} entity type is {{entity}} suitable.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</b></u><br>
    Before using derivatives, entities generally need brokerage accounts with margin approval, risk management policies, board authorization (for corporations), collateral or margin capacity, and legal review of derivative contracts. Derivatives require strong financial oversight. {{preraise}} reflects {{preraise}} pre-capital needs.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</b></u><br>
    Public derivatives trade on regulated exchanges such as Chicago Mercantile Exchange (CME), Cboe Global Markets, and New York Stock Exchange (for listed options). Regulatory oversight is provided by the U.S. Securities and Exchange Commission and the Commodity Futures Trading Commission (CFTC), depending on instrument type. {{premarket}} reflects {{premarket}} market positioning.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</b></u><br>
    Derivatives are not typically used to raise primary capital like equity or debt. However, they can be used to create synthetic leverage, monetize positions, hedge exposure, or structure convertible or structured products. Transaction sizes range from modest hedging contracts to multi-billion-dollar institutional trades. {{raisegoal}} is {{raisegoal}} typical for derivatives.
    </p>
    <p><b><u>6 – Capital Round Assessment</b></u><br>
    Derivatives do not represent ownership issuance. Common instruments include options, futures contracts, swaps, forwards, and warrants. They may complement equity or debt raises but are not standalone equity rounds. {{tranch}} is {{tranch}} relevant.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</b></u><br>
    Derivative contracts are structured based on expiration dates, settlement terms, margin requirements, and contract size. They can be entered into at any time market conditions permit. {{rounds}} reflects {{rounds}} timing flexibility.
    </p>
    <p><b><u>8 – Use of Funds Assessment</b></u><br>
    Use cases include hedging commodity price risk, managing currency exposure, interest rate risk mitigation, leveraged investment strategies, and structured capital solutions. Improper use can significantly increase financial risk. {{useoffund}} represents {{useoffund}} typical use cases.
    </p>
    <p><b><u>9 – Risk Assessment</b></u><br>
    Risk level: High to Extremely High. Risks include market volatility, leverage amplification of losses, margin calls, liquidity risk, and counterparty risk (OTC derivatives). Derivatives can produce losses exceeding initial investment.
    </p>
    <p><b><u>10 – Capital Cost Assessment</b></u><br>
    Costs may include margin requirements, premium payments (for options), brokerage commissions, clearing fees, and collateral posting. Leverage magnifies both returns and risk. {{enterprisecost}} reflects {{enterprisecost}} cost considerations.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</b></u><br>
    Upfront costs vary by instrument. Options require premium payment, futures require margin deposit, swaps may require collateral agreements. Institutional documentation and ISDA agreements may be required for OTC derivatives. {{upfrontcost}} is {{upfrontcost}} typical.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</b></u><br>
    Timing is immediate to short-term, as derivatives can be executed quickly once accounts are approved. However, structuring complex derivative strategies may take weeks for documentation and counterparty negotiation. {{upfronttime}} reflects {{upfronttime}} expected timing.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
