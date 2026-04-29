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

def publicsecuritiesmoneymarketinstruments(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Public Securities </b></u><br>
    Capital Type: Money Market Instruments </center></p>
    <p><b><u>Introduction</u></b><br>
    Money market instruments are short-term debt securities with maturities typically of one year or less, used by governments, financial institutions, and corporations to meet short-term funding needs. {n} fits that definition. These instruments are considered highly liquid and relatively low risk compared to long-term securities. They play a critical role in maintaining liquidity in the financial system and are widely used by institutional investors, corporations, and money market funds. In the United States, money market instruments are regulated under federal securities laws and supervised by the U.S. Securities and Exchange Commission.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. Money market instruments are debt securities issued for short durations, typically ranging from overnight to 12 months. Common examples include U.S. Treasury bills issued by the U.S. Department of the Treasury, commercial paper issued by corporations, certificates of deposit (CDs) issued by banks, and repurchase agreements (repos). These instruments are usually issued at a discount and redeemed at face value, providing a return based on the difference. They are designed for capital preservation and liquidity rather than high yield.<br>
    <br>
    2. Money market instruments are best suited for governments, banks, and large corporations requiring short-term working capital financing. Investors typically include institutional investors, mutual funds, pension funds, corporations managing cash reserves, and conservative individual investors seeking stable returns. Money market mutual funds, regulated under the Investment Company Act of 1940, invest primarily in these instruments to maintain liquidity and minimize volatility.<br>
    <br>
    3. Money market securities are subject to the Securities Act of 1933 and the Securities Exchange Act of 1934, depending on structure and issuance method. Certain instruments, such as Treasury bills, are exempt from registration. The SEC establishes rules for money market funds under Rule 2a-7, which governs portfolio quality, maturity limits, diversification, and liquidity requirements to protect investors and maintain market stability.<br>
    <br>
    4. Although considered low risk, money market instruments are subject to interest rate risk, credit risk (particularly commercial paper), inflation risk, and liquidity risk during market stress. Historically, disruptions such as the 2008 financial crisis demonstrated that even money market funds can experience pressure. While government-backed instruments are generally secure, privately issued instruments depend on issuer creditworthiness.<br>
    <br>
    5. Issuers must demonstrate strong creditworthiness and short-term repayment capacity to access money market funding at favorable rates. High credit ratings from agencies improve market acceptance. Investors evaluate maturity, yield, issuer strength, and market liquidity. Effective risk management, diversified holdings, and adherence to regulatory requirements are essential for maintaining investor confidence and market stability.
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Compliance with the Securities Act of 1933 (unless exempt)<br>
    · Disclosure Requirements for Non-Exempt Instruments<br>
    · SEC Rule 2a-7 Compliance (for Money Market Funds)<br>
    · Credit Rating (if applicable)<br>
    · Corporate Authorization for Debt Issuance<br>
    · AML/KYC Compliance
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    · Offering Memorandum or Disclosure Statement<br>
    · Commercial Paper Agreement (if applicable)<br>
    · Treasury Auction Documentation (for T-bills)<br>
    · Credit Rating Report<br>
    · Subscription Agreement<br>
    · Financial Statements<br>
    · Corporate Board Resolution Authorizing Issuance<br>
    · Risk Disclosure Statement
    </p>
    <p><u><b>References</b></u><br>
    1. U.S. Securities and Exchange Commission. (2023). Money Market Funds and Regulation. https://www.sec.gov/divisions/investment/mmf.shtml<br>
    2. U.S. Department of the Treasury. (n.d.). Treasury Bills Overview. https://home.treasury.gov<br>
    3. Investment Company Act of 1940. https://www.sec.gov/about/laws/ica40.pdf<br>
    4. Securities Act of 1933. https://www.sec.gov/about/laws/sa33.pdf<br>
    5. Investopedia. (n.d.). Money Market Instruments Definition. https://www.investopedia.com/terms/m/moneymarket.asp
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def publicsecuritiesmoneymarketinstrumentsfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Public Securities<br>
    Money Market Instruments</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What are money market instruments?</u></b><br>
    • Answer: Money market instruments are short-term debt securities with maturities of one year or less, used to provide liquidity and low-risk investment options.
    </p>
    <p><u><b>2. What is the purpose of money market instruments?</u></b><br>
    • Answer: They are used by governments, financial institutions, and corporations to manage short-term funding needs and working capital.
    </p>
    <p><u><b>3. What are common types of money market instruments?</u></b><br>
    • Answer: Common types include Treasury bills, commercial paper, certificates of deposit, repurchase agreements, and bankers' acceptances.
    </p>
    <p><u><b>4. What are Treasury bills?</u></b><br>
    • Answer: Treasury bills (T-bills) are short-term government securities issued by the U.S. Department of the Treasury with maturities ranging from a few days to one year.
    </p>
    <p><u><b>5. What is commercial paper?</u></b><br>
    • Answer: Commercial paper is an unsecured, short-term corporate debt instrument issued by large companies to finance operational expenses.
    </p>
    <p><u><b>6. What are certificates of deposit (CDs)?</u></b><br>
    • Answer: Certificates of deposit are time deposits offered by banks that pay interest for holding funds for a fixed short-term period.
    </p>
    <p><u><b>7. What are repurchase agreements (repos)?</u></b><br>
    • Answer: Repos are short-term borrowing agreements where securities are sold with a commitment to repurchase them at a later date, often used by financial institutions.
    </p>
    <p><u><b>8. What is a banker's acceptance?</u></b><br>
    • Answer: A banker's acceptance is a short-term debt instrument guaranteed by a bank, commonly used in international trade transactions.
    </p>
    <p><u><b>9. Are money market instruments considered safe?</u></b><br>
    • Answer: They are generally considered low-risk, especially government-issued instruments, but they are not entirely risk-free.
    </p>
    <p><u><b>10. How do investors earn returns on money market instruments?</u></b><br>
    • Answer: Returns are earned through interest payments or by purchasing the instrument at a discount and receiving full face value at maturity.
    </p>
    <p><u><b>11. Who typically invests in money market instruments?</u></b><br>
    • Answer: Institutional investors, corporations, banks, and conservative individual investors often use them for capital preservation and liquidity.
    </p>
    <p><u><b>12. What is the difference between money markets and capital markets?</u></b><br>
    • Answer: Money markets focus on short-term debt instruments, while capital markets handle long-term securities such as stocks and bonds.
    </p>
    <p><u><b>13. Are money market instruments publicly traded?</u></b><br>
    • Answer: Yes, many are traded in public financial markets or over-the-counter markets.
    </p>
    <p><u><b>14. How do money market instruments impact liquidity?</u></b><br>
    • Answer: They enhance financial system liquidity by enabling efficient short-term borrowing and lending.
    </p>
    <p><u><b>15. When should a business use money market instruments?</u></b><br>
    • Answer: A business should use money market instruments when managing short-term cash flow needs or temporarily investing surplus cash.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def publicsecuritiesmoneymarketinstrumentstwelve(request):
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
    Capital Type: Money Market Instruments</p></center>
    <p><b><u>1 - Stage of Development Assessment</u></b><br>
    Money market instruments are best suited for:<br>
    · Established corporations<br>
    · Financial institutions<br>
    · Governments and municipalities<br>
    · Public companies with strong credit profiles<br>
    Early-stage startups generally do not qualify due to creditworthiness requirements.
    </p>
    <p><b><u>2 - Entity Type Assessment</u></b><br>
    Most appropriate for:<br>
    · Public C-Corporations<br>
    · Banks and financial institutions<br>
    · Government entities<br>
    · Large private corporations with strong balance sheets<br>
    Issuers must demonstrate high short-term credit quality.
    </p>
    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    Before issuing money market instruments, companies typically require:<br>
    · Strong audited financials<br>
    · Investment-grade credit profile (in many cases)<br>
    · Established banking relationships<br>
    · Commercial paper programs (if applicable)<br>
    Issuance is typically supported by backup credit facilities.
    </p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    Money market instruments trade in regulated public markets under oversight from the U.S. Securities and Exchange Commission.
    Common instruments include:<br>
    · Treasury Bills issued by the U.S. Department of the Treasury<br>
    · Commercial Paper<br>
    · Certificates of Deposit (CDs)<br>
    · Repurchase Agreements (Repos)<br>
    · Banker's Acceptances<br>
    These instruments are widely traded in institutional fixed-income markets.
    </p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    Issuance size varies widely:<br>
    · Commercial paper programs often range from $50 million to several billion dollars<br>
    · Government Treasury bill issuance can reach significantly larger volumes<br>
    Minimum issuance amounts are typically institutional-scale.
    </p>
    <p><b><u>6 - Capital Round Assessment</u></b><br>
    Money market instruments are:<br>
    · Short-term debt obligations<br>
    · Typically unsecured (commercial paper)<br>
    · Issued at a discount and redeemed at face value<br>
    They do not involve equity or ownership dilution.
    </p>
    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    Issuance may occur:<br>
    · On a rolling basis<br>
    · In periodic auctions (Treasury bills)<br>
    · As needed for working capital<br>
    Maturities generally range from overnight to 12 months.
    </p>
    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    Common uses include:<br>
    · Working capital<br>
    · Payroll<br>
    · Inventory financing<br>
    · Bridge liquidity<br>
    · Short-term operational needs<br>
    Not intended for long-term capital projects.
    </p>
    <p><b><u>9 - Risk Assessment</u></b><br>
    Risk level: Low to Moderate, depending on issuer.
    Risks include:<br>
    · Refinancing risk at maturity<br>
    · Interest rate fluctuations<br>
    · Liquidity disruptions<br>
    · Credit downgrade risk<br>
    Government-issued instruments are generally considered lower risk than corporate commercial paper.
    </p>
    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    Costs typically include:<br>
    · Discount rate (interest cost)<br>
    · Dealer placement fees<br>
    · Credit facility fees (if required)<br>
    Rates are generally lower than long-term corporate bonds due to short maturities.
    </p>
    <p><b><u>11 - Up Front Cost Assessment</u></b><br>
    Upfront costs may include:<br>
    · Legal structuring<br>
    · Dealer agreements<br>
    · Credit rating fees<br>
    · Backup line of credit establishment<br>
    Costs are moderate but manageable for large issuers.
    </p>
    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
    Timing is very fast once a program is established.
    Funds can often be raised within days or even same-day settlement, depending on instrument and market conditions.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
