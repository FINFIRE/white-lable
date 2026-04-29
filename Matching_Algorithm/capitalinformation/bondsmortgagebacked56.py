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

def bondsmortgagebacked(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Bonds</b></u><br>
    Capital Type: Mortgage Backed </center></p>
    <p><b><u>Introduction</u></b><br>
Mortgage-Backed Bonds are ideal for investors seeking fixed-income exposure supported by pools of real estate loans. They are designed so that capital is raised through the securitization of residential or commercial mortgages, with investors receiving cash flows derived from the principal and interest payments made by underlying borrowers. {n} fits that definition. In 2026, mortgage-backed securities (MBS) remain a core segment of global structured finance markets, providing liquidity to housing and commercial real estate sectors. These instruments include agency-backed securities issued or guaranteed by government-sponsored entities and private-label mortgage-backed bonds structured by financial institutions. They are widely used by institutional investors for yield enhancement and portfolio diversification. While mortgage-backed bonds offer predictable cash flows, they are exposed to prepayment risk, interest-rate sensitivity, and credit risk. Changes in borrower behavior, refinancing activity, or real estate market conditions can materially affect timing and magnitude of investor returns.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.A Mortgage-Backed Bond is a fixed-income security created by pooling mortgage loans and selling interests in the resulting cash flows to investors. Payments to bondholders are derived from the scheduled principal and interest payments made by mortgage borrowers. (Investopedia, 2025)
<br>


    <br>2.  Mortgage-backed bonds occupy a structured position within the Capital Stack, with payment priority determined by tranche seniority. Senior tranches receive cash flows first and carry lower risk, while junior tranches absorb losses first and offer higher yields. (Corporate Finance Institute, 2026)
<br>

    <br>3. Legally, mortgage-backed bonds are issued through a Securitization Trust governed by a Pooling and Servicing Agreement (PSA) that defines loan eligibility, servicing standards, payment waterfalls, and investor rights. Agency-backed securities carry explicit or implicit government guarantees. (Federal Reserve Bank of St. Louis, 2025)
<br>
    <br>4.From a risk perspective, mortgage-backed bonds introduce prepayment, extension, and credit risk. Falling interest rates increase prepayments and shorten duration, while rising rates extend maturities and increase duration risk, particularly for fixed-rate pools. (Bank for International Settlements, 2025)
<br>
    <br>5.
From an accounting and process standpoint, mortgage-backed bonds are recorded as Debt Securities by issuers and as Fixed-Income Investments by investors. Cash flows are distributed monthly, and pricing is influenced by interest-rate expectations, housing market trends, and borrower credit performance. (Deloitte, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Investopedia. (2025). Mortgage-Backed Securities (MBS). <a href="https://www.investopedia.com/mortgage-backed-securities">https://www.investopedia.com/mortgage-backed-securities</a>
<br>
    <br>Corporate Finance Institute (CFI). (2026). Mortgage-Backed Securities Explained. <a href="https://corporatefinanceinstitute.com/resources/credit-analysis">https://corporatefinanceinstitute.com/resources/credit-analysis</a>
<br>
    <br>Federal Reserve Bank of St. Louis. (2025). Mortgage Markets and Securitization. <a href="https://fred.stlouisfed.org">https://fred.stlouisfed.org</a>
<br>
    <br>Bank for International Settlements (BIS). (2025). Structured Finance and Interest Rate Risk. <a href="https://www.bis.org">https://www.bis.org</a>
<br>
    <br>Deloitte. (2025). Accounting for Securitized Debt Instruments. <a href="https://www2.deloitte.com/securitization">https://www2.deloitte.com/securitization</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Mortgage Pool Eligibility - Residential or commercial mortgage loans
<br>•   Loan Underwriting Standards - Credit, LTV, and documentation requirements
<br>•   Securitization Structure - Trust or special-purpose vehicle (SPV)
<br>•   Tranching & Waterfall Rules - Payment priority and loss allocation
<br>•   Servicing & Trustee Agreements - Loan administration and oversight
<br>•   Disclosure & Reporting - Pool performance and investor reporting
<br>•   Regulatory Compliance - Securities and structured finance regulations
<br>•   Rating Agency Review - Tranche-level credit assessment


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Offering Circular / Prospectus - Security disclosures
<br>•   Pooling & Servicing Agreement (PSA) - Cash flow mechanics
<br>•   Mortgage Loan Schedule - Loan-level data
<br>•   Servicer Agreement - Collection and servicing obligations
<br>•   Trustee Agreement - Fiduciary oversight
<br>•   Rating Agency Reports - Tranche credit ratings
<br>•   Legal Opinions - Bankruptcy remoteness and enforceability
<br>•   Cash Flow Models - Prepayment and loss assumptions

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def bondsmortgagebackedfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Bonds<br>
    Mortgage Backed</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What are mortgage-backed bonds?</u></b><br>
    •Answer: Mortgage-backed bonds, also known as mortgage-backed securities (MBS), are debt instruments backed by pools of residential or commercial mortgage loans.
</p>

    <p><u><b>2. Who issues mortgage-backed bonds?</u></b><br>
    •Answer: They are issued by government-sponsored entities, financial institutions, or special purpose vehicles that bundle mortgage loans.
</p>

    <p><u><b>3. When are mortgage-backed bonds typically used?</u></b><br>
    •Answer: They are used to provide liquidity to mortgage lenders and to channel investor capital into housing and real estate markets.
</p>

    <p><u><b>4. How do mortgage-backed bonds work?</u></b><br>
    •Answer: Investors receive periodic payments derived from the principal and interest payments made by homeowners on the underlying mortgages.
</p>

    <p><u><b>5. What types of mortgages back these bonds?</u></b><br>
    •Answer: They can be backed by residential mortgages, commercial mortgages, or a mix of both, depending on the structure.
</p>

    <p><u><b>6. Are there different types of mortgage-backed bonds?</u></b><br>
    •Answer: Yes, common types include pass-through securities, collateralized mortgage obligations (CMOs), and commercial mortgage-backed securities (CMBS).
</p>

    <p><u><b>7. Do mortgage-backed bonds pay regular income?</u></b><br>
    •Answer: Yes, they typically pay monthly or periodic income consisting of both interest and principal.
</p>

    <p><u><b>8. What is prepayment risk in mortgage-backed bonds?</u></b><br>
    •Answer: Prepayment risk occurs when borrowers repay mortgages early, which can reduce expected interest income for investors.
</p>

    <p><u><b>9. How are interest rates determined for mortgage-backed bonds?</u></b><br>
    •Answer: Rates depend on underlying mortgage rates, credit quality, prepayment risk, and overall market conditions.
</p>

    <p><u><b>10. Are mortgage-backed bonds considered low risk?</u></b><br>
    •Answer: Risk levels vary; government-backed MBS are lower risk, while private-label MBS carry higher credit and structural risk.
</p>

    <p><u><b>11. Can mortgage-backed bonds be traded?</u></b><br>
    •Answer: Yes, they are actively traded in secondary markets, though liquidity varies by type.
</p>

    <p><u><b>12. What are the benefits of investing in mortgage-backed bonds?</u></b><br>
    •Answer: Benefits include regular income, diversification, and exposure to real estate-related cash flows.
</p>

    <p><u><b>13. What risks are associated with mortgage-backed bonds?</u></b><br>
    •Answer: Risks include prepayment risk, interest rate risk, credit risk, and structural complexity.
</p>

    <p><u><b>14. How do mortgage-backed bonds differ from traditional bonds?</u></b><br>
    •Answer: Unlike traditional bonds with fixed payments, MBS payments depend on mortgage cash flows and borrower behavior.
</p>

    <p><u><b>15. When should investors consider mortgage-backed bonds?</u></b><br>
    •Answer: Investors should consider them when seeking income diversification and are comfortable with interest rate and prepayment risks.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def bondsmortgagebackedtwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Bonds</b></u><br>
    Capital Type: Mortgage Backed</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Mortgage-backed bonds are best suited for mature financial institutions, real estate companies, or special-purpose entities that manage pools of mortgage assets. These instruments are not appropriate for early-stage startups, as issuers must have established mortgage origination, servicing capabilities, and predictable cash flows tied to underlying real estate assets.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Issuers are typically C-Corporations, financial institutions, real estate investment entities, or special purpose vehicles created specifically to hold and securitize mortgage assets. LLCs may be used in certain structures, but sole proprietorships are not suitable due to regulatory, disclosure, and scale requirements.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Issuers of mortgage-backed bonds generally have significant prior capitalization and an existing portfolio of mortgage loans. Underwriting focuses on the quality, diversification, and performance history of the mortgage pool rather than venture-style equity funding history.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Mortgage-backed bonds operate within the structured finance and fixed income capital markets and are typically issued in public or private markets. Investors include institutional asset managers, pension funds, insurance companies, and other fixed income investors seeking yield backed by real estate cash flows.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Capital raised through mortgage-backed bond issuances is typically large in scale, ranging from tens of millions to billions of dollars, depending on the size and value of the underlying mortgage pool. Issuance size is directly tied to asset volume and market demand.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Mortgage-backed bonds are not capital rounds and do not involve equity issuance. They are structured as debt securities with defined maturities and payment structures supported by cash flows from underlying mortgage assets.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Issuances are commonly structured with multiple tranches, each with different seniority, risk profiles, maturities, and interest rates. Tranching allows issuers to appeal to a broad range of investors while allocating risk based on credit enhancement structures.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Proceeds from mortgage-backed bonds are generally used to finance or refinance mortgage portfolios, support ongoing loan origination, or free up capital for additional lending activity. Use of funds is directly tied to real estate-backed lending operations.
<br>•   Finance or refinance mortgage portfolios
<br>•   Support ongoing loan origination
<br>•   Free up capital for additional lending activity

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Investor risk includes exposure to borrower defaults, prepayment risk, interest rate volatility, and real estate market fluctuations. Issuers face operational, servicing, and compliance risks, as well as potential reputational risk if asset performance deteriorates.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital varies by tranche and credit quality but is generally lower than unsecured debt due to asset backing. Costs include interest payments, structuring fees, credit enhancement expenses, and ongoing servicing and administration costs.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are high and include legal and structural setup, ratings agency fees, underwriting costs, due diligence on mortgage pools, and regulatory compliance expenses. These costs are typically justified by the scale and efficiency of securitized financing.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital is relatively long due to the complexity of structuring, regulatory review, and investor marketing. The process typically takes several months from asset pooling to issuance and settlement.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
