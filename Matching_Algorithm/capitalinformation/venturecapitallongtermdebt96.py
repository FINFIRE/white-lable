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

def venturecapitallongtermdebt(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Venture Capital</b></u><br>
    Capital Type: Long Term Debt </center></p>
    <p><b><u>Introduction</u></b><br>
    Venture capital long-term debt refers to financing provided to high-growth or venture-backed companies in the form of long maturity loans rather than equity investment. {n} fits that definition. Unlike traditional venture capital equity funding, venture debt allows startups to access additional capital without immediate ownership dilution. These loans are typically provided alongside equity financing rounds and are structured with higher interest rates due to the risk profile of early-stage companies. In the United States, venture lending activities are generally structured under the regulatory framework of the Securities Act of 1933 when the debt instrument is considered a security.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. Venture long-term debt is a financing mechanism that provides startups with working capital, expansion funding, or operational liquidity without requiring equity issuance. These loans typically have maturity periods ranging from three to seven years and may include interest-only payment periods during the early stages. Some venture lenders also attach warrants or conversion rights to participate in future company appreciation.<br><br>
    2. Venture long-term debt is best suited for venture-backed startups with predictable revenue streams, strong investor backing, and proven business models. Technology companies, SaaS businesses, biotech firms, and high-growth enterprises often use venture debt to extend their cash runway after equity fundraising rounds. Companies should have sufficient collateral value or institutional sponsorship to qualify.<br><br>
    3. Venture debt financing may fall under securities regulation if structured as an investment contract or debt security offering. Lending institutions providing venture loans must comply with federal financial regulations under the supervision of the U.S. Securities and Exchange Commission when the instrument is marketed as a security. Commercial lending standards and credit underwriting processes are also applied depending on the structure.<br><br>
    4. Long-term venture debt carries repayment obligations regardless of business performance, increasing financial pressure during revenue downturns. Interest costs and covenant requirements may restrict operational flexibility. Default risk is higher than traditional bank loans due to the early-stage nature of borrowing companies. Additionally, lenders may require warrants or equity kickers to compensate for risk exposure.<br><br>
    5. To obtain venture long-term debt, companies must demonstrate revenue stability, strong investor relationships, and positive growth projections. Financial documentation, business forecasts, and collateral evaluation are typically required. Successful applicants usually maintain good credit profiles, experienced management teams, and clear exit strategies.
    </p>
     <p><u><b>References</u></b><br>
    1. U.S. Securities and Exchange Commission. (2023). https://www.sec.gov<br>
    2. National Venture Capital Association. (n.d.). https://nvca.org<br>
    3. Investopedia. (n.d.). Venture Debt Definition. https://www.investopedia.com/terms/v/venture-debt.asp<br>
    4. Harvard Business Review. (2020). Startup Financing Strategies. https://hbr.org<br>
    5. Corporate Finance Institute. (n.d.). https://corporatefinanceinstitute.com
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    • Compliance with the Securities Act of 1933<br>
    • Proper Debt Instrument Structuring<br>
    • AML/KYC Verification<br>
    • Corporate Authorization for Borrowing<br>
    • Financial Disclosure Requirements<br>
    • Interest Rate and Covenant Agreement<br>
    • Accredited or Institutional Lender Participation
    </p>
                             
    <p><u><b>Supporting Document List</u></b><br>
    • Loan Agreement<br>
    • Financial Statements<br>
    • Business Plan and Revenue Forecast<br>
    • Collateral Documentation (if required)<br>
    • Investor / Venture Partner Agreement<br>
    • Board Resolution Authorizing Debt<br>
    • Risk Disclosure Statement<br>
    • Capitalization Table
    </p>
    """)
    introduction =introduction.format(n=name)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def venturecapitallongtermdebtfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Venture Capital<br>
    Long Term Debt</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is long-term debt in venture capital financing?</u></b><br>
    • Answer: Long-term venture debt is a financing instrument provided to growth-stage startups, allowing them to access capital while delaying full equity dilution.
    </p>
    <p><u><b>2. Who provides venture long-term debt?</u></b><br>
    • Answer: Venture debt is usually provided by specialized venture debt funds, commercial banks with startup divisions, or institutional lenders.
    </p>
    <p><u><b>3. What is the typical purpose of venture long-term debt?</u></b><br>
    • Answer: It is commonly used for expansion, product development, working capital support, or extending the runway between equity funding rounds.
    </p>
    <p><u><b>4. How long are the repayment terms?</u></b><br>
    • Answer: Repayment periods typically range from 2 to 7 years depending on the company's cash flow and risk profile.
    </p>
    <p><u><b>5. Is collateral required for venture long-term debt?</u></b><br>
    • Answer: Collateral requirements vary but may include intellectual property, company assets, or future receivables.
    </p>
    <p><u><b>6. Does venture long-term debt require equity dilution?</u></b><br>
    • Answer: Venture debt generally does not require immediate equity dilution, though warrants or conversion options may be included.
    </p>
    <p><u><b>7. What interest rates apply to venture long-term debt?</u></b><br>
    • Answer: Interest rates are usually higher than traditional bank loans but lower than pure equity financing costs.
    </p>
    <p><u><b>8. Who is eligible for venture long-term debt?</u></b><br>
    • Answer: Growth-stage startups with venture backing, predictable revenue, or strong future growth potential are typically eligible.
    </p>
    <p><u><b>9. How quickly can venture debt be obtained?</u></b><br>
    • Answer: Funding can be obtained faster than equity rounds, often within weeks after due diligence.
    </p>
    <p><u><b>10. What are the advantages of venture long-term debt?</u></b><br>
    • Answer: Advantages include preserving ownership, extending cash runway, and accessing capital without full equity dilution.
    </p>
    <p><u><b>11. What are the risks of venture long-term debt?</u></b><br>
    • Answer: Risks include repayment pressure, covenant restrictions, and potential default if projected growth does not materialize.
    </p>
    <p><u><b>12. Can venture debt be combined with equity financing?</u></b><br>
    • Answer: Yes, it is often used alongside venture capital equity funding rounds.
    </p>
    <p><u><b>13. Are startups without revenue eligible?</u></b><br>
    • Answer: Early pre-revenue startups may face difficulty unless they have strong venture backing or asset security.
    </p>
    <p><u><b>14. How is venture debt repayment structured?</u></b><br>
    • Answer: Repayment may include monthly interest payments with principal repayment later in the term.
    </p>
    <p><u><b>15. When should a company consider venture long-term debt?</u></b><br>
    • Answer: Companies should consider venture debt when they need growth capital while minimizing ownership dilution and have confidence in future cash flows.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def venturecapitallongtermdebttwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Venture Capital</b></u><br>
    Capital Type: Long Term Debt</p></center>
    <p><b><u>1 – Stage of Development Assessment</u></b><br>
    Venture capital long-term debt is best suited for growth-stage and late-stage venture-backed companies that have: Stable or improving cash flow; Institutional or angel equity backing; Predictable future revenue streams. It is less common for early-stage startups without operating traction.
    </p>
    <p><b><u>2 – Entity Type Assessment</u></b><br>
    Most appropriate for: C-Corporations; Venture-backed technology companies; Scalable high-growth enterprises. Lenders usually require formal governance structure and equity sponsor support.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</u></b><br>
    Before approval, companies typically need: Financial projections and historical performance; Existing equity investor validation; Collateral or intellectual property security (in some cases); Defined repayment strategy. Many venture debt facilities require a relationship with existing venture investors.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</u></b><br>
    Venture long-term debt operates in the private credit and venture lending market, often provided by: Venture debt funds; Specialized growth lenders; Technology-focused financing institutions. These transactions are generally structured as private financing agreements.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</u></b><br>
    Typical facility sizes range from $1 million to $50 million, though larger facilities are possible for highly valued technology companies. Debt size is often linked to: Revenue scale; Venture equity backing; Cash flow stability.
    </p>
    <p><b><u>6 – Capital Round Assessment</u></b><br>
    Venture long-term debt is non-dilutive debt financing but may include: Warrants; Conversion rights; Equity participation features. It is often used alongside equity rounds.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</u></b><br>
    Funding is commonly structured as: Initial draw at closing; Subsequent milestone-based draws; Revolving or term loan structures. Draws may depend on performance covenants.
    </p>
    <p><b><u>8 – Use of Funds Assessment</u></b><br>
    Typical uses include: Product expansion; Market scaling; Working capital support; Hiring and infrastructure development; Bridge-to-equity financing. Funds are generally restricted from speculative investments.
    </p>
    <p><b><u>9 – Risk Assessment</u></b><br>
    Risk level: Moderate to High. Risks include: Debt repayment pressure on growing companies; Conversion or warrant dilution risk; Revenue volatility; Covenant compliance requirements. Lenders rely on venture sponsor credibility.
    </p>
    <p><b><u>10 – Capital Cost Assessment</u></b><br>
    Cost of capital is higher than traditional bank loans but lower than pure equity financing. Costs may include: Interest rates typically 8%–20%; Warrant coverage or equity kicker; Origination and monitoring fees.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</u></b><br>
    Upfront costs are moderate, including: Legal documentation; Financial review; Due diligence fees; Facility structuring expenses.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</u></b><br>
    Timing is relatively fast, usually 1–3 months, depending on: Existing investor relationships; Financial readiness; Negotiation of loan covenants.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
