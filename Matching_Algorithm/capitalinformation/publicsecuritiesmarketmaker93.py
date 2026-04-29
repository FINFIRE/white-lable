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

def publicsecuritiesmarketmaker(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Public Securities </b></u><br>
    Capital Type: Market Maker </center></p>
    <p><b><u>Introduction</u></b><br>
    A market maker is a registered financial firm or broker-dealer that continuously quotes both buy (bid) and sell (ask) prices for publicly traded securities to provide liquidity and facilitate orderly market trading. {n} fits that definition. Market makers play a central role in public securities markets by ensuring that investors can buy and sell securities efficiently, even when natural counterparties are not immediately available. In the United States, market makers operate under the oversight of the U.S. Securities and Exchange Commission and must comply with rules established by the Financial Industry Regulatory Authority (FINRA). Their activities promote price discovery, market efficiency, and trading stability.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. A market maker is typically a broker-dealer that stands ready to buy and sell a specific security on a regular and continuous basis at publicly quoted prices. By maintaining two-sided quotes, market makers profit from the bid-ask spread while assuming short-term inventory risk. They may operate on national securities exchanges such as New York Stock Exchange or NASDAQ, or in over-the-counter (OTC) markets. Their role enhances liquidity and reduces transaction costs for investors (SEC, 2023).<br>
    <br>
    2. Market makers are typically large broker-dealers, investment banks, and proprietary trading firms with sufficient capital, advanced trading systems, and regulatory approvals. Companies whose securities are publicly traded benefit from designated market makers because increased liquidity improves trading volume, investor confidence, and price stability. Smaller or newly listed securities particularly rely on market makers to maintain active trading markets.<br>
    <br>
    3. Market making activities are governed under the Securities Exchange Act of 1934, which established the regulatory framework for securities trading and broker-dealer conduct. Market makers must comply with SEC rules regarding fair dealing, best execution, capital requirements, and anti-manipulation provisions. FINRA oversees quoting practices and trading compliance to ensure transparent and orderly markets.<br>
    <br>
    4. Market makers assume inventory risk, meaning they may incur losses if the price of a security moves unfavorably while holding positions. During periods of extreme volatility or low liquidity, spreads may widen, increasing trading costs for investors. Regulatory scrutiny is significant, and violations of quoting or trading rules may result in fines or sanctions. Additionally, algorithmic trading competition has compressed spreads, reducing profitability margins.<br>
    <br>
    5. To operate as a market maker, a broker-dealer must register with the SEC, obtain FINRA membership, meet net capital requirements, and comply with exchange-specific rules. Firms must maintain adequate risk management systems, real-time trading infrastructure, and compliance controls. Successful market makers rely on sophisticated trading algorithms, liquidity modeling, and disciplined inventory management to balance profitability and regulatory compliance.
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · SEC Registration as Broker-Dealer<br>
    · FINRA Membership Approval<br>
    · Compliance with the Securities Exchange Act of 1934<br>
    · Exchange Membership (e.g., NYSE or NASDAQ, if applicable)<br>
    · Net Capital Requirements<br>
    · Best Execution and Fair Dealing Compliance<br>
    · AML/KYC Compliance<br>
    · Ongoing Regulatory Reporting
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    · Broker-Dealer Registration (Form BD)<br>
    · FINRA Membership Application<br>
    · Exchange Market Maker Agreement<br>
    · Net Capital Compliance Reports<br>
    · Risk Management Policy<br>
    · Trading Supervision Procedures<br>
    · Best Execution Policy<br>
    · AML Compliance Program Documentation
    </p>
    <p><u><b>References</b></u><br>
    1. U.S. Securities and Exchange Commission. (2023). Market Makers and Liquidity. https://www.sec.gov/education/smallbusiness/goingpublic/marketmakers<br>
    2. Financial Industry Regulatory Authority. (n.d.). Market Maker Requirements. https://www.finra.org/rules-guidance<br>
    3. Securities Exchange Act of 1934. (1934). https://www.sec.gov/about/laws/sea34.pdf<br>
    4. New York Stock Exchange. (n.d.). Designated Market Maker (DMM) Overview. https://www.nyse.com/markets/nyse/designated-market-makers<br>
    5. Investopedia. (n.d.). Market Maker Definition. https://www.investopedia.com/terms/m/marketmaker.asp
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def publicsecuritiesmarketmakerfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Public Securities <br>
    Market Maker</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is a market maker?</u></b><br>
    • Answer: A market maker is a financial firm or broker-dealer that provides liquidity to public markets by continuously quoting both buy and sell prices for securities.
    </p>
    <p><u><b>2. How does a market maker operate?</u></b><br>
    • Answer: A market maker profits from the bid-ask spread by purchasing securities at the bid price and selling them at the ask price.
    </p>
    <p><u><b>3. Why are market makers important in public markets?</u></b><br>
    • Answer: Market makers help ensure liquidity, reduce price volatility, and facilitate smoother trading in exchanges such as the New York Stock Exchange and NASDAQ.
    </p>
    <p><u><b>4. What types of securities do market makers trade?</u></b><br>
    • Answer: They trade equities, options, ETFs, bonds, and sometimes derivatives in public markets.
    </p>
    <p><u><b>5. How do market makers manage risk?</u></b><br>
    • Answer: They use hedging strategies, inventory controls, and algorithmic trading systems to manage exposure to price fluctuations.
    </p>
    <p><u><b>6. Are market makers regulated?</u></b><br>
    • Answer: Yes, market makers are regulated by authorities such as the U.S. Securities and Exchange Commission and self-regulatory organizations like Financial Industry Regulatory Authority.
    </p>
    <p><u><b>7. Do market makers use their own capital?</u></b><br>
    • Answer: Yes, they use firm capital to hold inventory and facilitate transactions.
    </p>
    <p><u><b>8. What is the bid-ask spread?</u></b><br>
    • Answer: The bid-ask spread is the difference between the price a market maker is willing to buy a security and the price at which it is willing to sell it.
    </p>
    <p><u><b>9. How do market makers earn revenue?</u></b><br>
    • Answer: Revenue is primarily generated from the bid-ask spread, trading volume, and sometimes exchange incentives.
    </p>
    <p><u><b>10. What is the difference between a broker and a market maker?</u></b><br>
    • Answer: A broker executes trades on behalf of clients, while a market maker provides liquidity by standing ready to buy and sell securities.
    </p>
    <p><u><b>11. Can market makers influence stock prices?</u></b><br>
    • Answer: While they provide liquidity, market makers must operate within regulatory guidelines and cannot legally manipulate prices.
    </p>
    <p><u><b>12. What is designated market making?</u></b><br>
    • Answer: Designated market makers are firms assigned by an exchange to maintain orderly markets for specific securities.
    </p>
    <p><u><b>13. Do electronic trading systems replace market makers?</u></b><br>
    • Answer: Many modern market makers use algorithmic and high-frequency trading systems to automate liquidity provision.
    </p>
    <p><u><b>14. Are market makers involved in IPOs?</u></b><br>
    • Answer: Yes, they may support post-IPO trading by providing liquidity and stabilizing price movements.
    </p>
    <p><u><b>15. When does a company benefit from market makers?</u></b><br>
    • Answer: A company benefits when market makers improve trading liquidity, price efficiency, and investor confidence in its publicly traded shares.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def publicsecuritiesmarketmakertwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Public Securities </b></u><br>
    Capital Type: Market Maker</p></center>
    <p><b><u>1 - Stage of Development Assessment</u></b><br>
    Market makers are relevant for:<br>
    · Publicly traded companies<br>
    · Newly listed IPOs<br>
    · SPAC post-merger entities<br>
    · Thinly traded micro-cap stocks<br>
    They are not a primary capital-raising source, but they support secondary market liquidity after securities are issued.
    </p>
    <p><b><u>2 - Entity Type Assessment</u></b><br>
    Applicable to:<br>
    · Public C-Corporations<br>
    · Exchange-listed companies<br>
    · OTC-traded companies<br>
    Market makers themselves must be registered broker-dealers.
    </p>
    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    Before engaging a market maker, a company must:<br>
    · Have publicly traded securities<br>
    · Be current with SEC reporting requirements<br>
    · Maintain a transfer agent<br>
    · Meet exchange or OTC compliance standards<br>
    Market makers require regulatory approval before quoting securities.
    </p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    Market makers operate in regulated securities markets under the oversight of the U.S. Securities and Exchange Commission and are members of Financial Industry Regulatory Authority (FINRA).
    They provide liquidity on exchanges such as:<br>
    · New York Stock Exchange<br>
    · Nasdaq<br>
    · OTC Markets platforms
    </p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    Market makers do not raise capital directly for the company.
    Instead, they:<br>
    · Provide bid and ask quotes<br>
    · Enhance trading volume<br>
    · Improve liquidity<br>
    · Help stabilize pricing<br>
    Capital raising occurs separately via public offerings.
    </p>
    <p><b><u>6 - Capital Round Assessment</u></b><br>
    Market makers participate only in the secondary market.
    They do not issue equity, debt, or new securities.
    However, improved liquidity can support future follow-on offerings.
    </p>
    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    There is no tranche schedule, as no capital is raised.
    Liquidity support is ongoing during market hours.
    </p>
    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    Companies may engage market makers to:<br>
    · Increase investor confidence<br>
    · Reduce bid-ask spreads<br>
    · Improve stock visibility<br>
    · Support post-IPO trading<br>
    This indirectly supports valuation stability.
    </p>
    <p><b><u>9 - Risk Assessment</u></b><br>
    Risk level: Moderate<br>
    Risks include:<br>
    · Artificial appearance of liquidity if poorly structured<br>
    · Regulatory scrutiny<br>
    · Volatility in low-float securities<br>
    · Dependence on trading volume<br>
    Market makers cannot guarantee stock price performance.
    </p>
    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    Costs may include:<br>
    · Monthly service fees (for OTC issuers)<br>
    · Retainer agreements<br>
    · Consulting arrangements<br>
    Exchanges like NYSE and Nasdaq often designate official market makers without issuer payment, while OTC issuers may directly engage firms.
    </p>
    <p><b><u>11 - Up Front Cost Assessment</u></b><br>
    Upfront costs are typically low to moderate, including:<br>
    · Engagement agreements<br>
    · Legal review<br>
    · Compliance verification<br>
    Compared to primary offerings, costs are minimal.
    </p>
    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
    Liquidity support can begin quickly once:<br>
    · Registration is active<br>
    · Market maker approval is granted<br>
    · Compliance is verified<br>
    There is no direct capital infusion timeline.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
