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

def bondsgovernmentbacked(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Bonds</b></u><br>
    Capital Type: Government Backed </center></p>
    <p><b><u>Introduction</u></b><br>
Government-Backed Bonds are ideal for investors seeking low-risk, stable-income instruments supported by the creditworthiness of a sovereign government or a government-sponsored entity. They are designed so that capital is raised by public-sector issuers to fund fiscal operations, infrastructure projects, social programs, or economic stabilization initiatives, with repayment guaranteed or supported by the government. {n} fits that definition. In 2026, government-backed bonds remain the foundation of global fixed-income markets, serving as benchmarks for risk-free rates, yield curves, and monetary policy transmission. These bonds include sovereign bonds, treasury securities, and obligations issued by government agencies or state-owned enterprises with explicit or implicit government guarantees. They play a central role in portfolio diversification, capital preservation, and institutional liquidity management. While government-backed bonds offer high credit quality and liquidity, they are exposed to interest rate, inflation, and sovereign risk. Changes in fiscal policy, monetary tightening, or geopolitical conditions can materially affect bond prices and real returns, particularly for long-duration securities.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.A Government-Backed Bond is a debt security issued or guaranteed by a national government or government-sponsored entity, obligating the issuer to pay periodic interest and return principal at maturity. These instruments are backed by the taxing authority or credit support of the sovereign, making them among the lowest-risk fixed-income assets. (International Monetary Fund, 2025)
<br>


    <br>2.  Government-backed bonds occupy the senior-most position in the Capital Stack, ranking ahead of corporate debt and equity in terms of perceived credit safety. In sovereign restructurings, these bonds are typically prioritized under public debt frameworks, though recovery outcomes depend on jurisdiction and legal structure. (World Bank, 2025)
<br>

    <br>3. Legally, government-backed bonds are governed by public debt statutes, issuance programs, and offering circulars that define coupon rates, maturities, payment schedules, and governing law. Issuance is typically conducted through auctions or syndications and settled through central securities depositories. (U.S. Treasury, 2025)
<br>
    <br>4.From a risk perspective, government-backed bonds minimize default risk but introduce interest rate risk, inflation risk, and currency risk. Rising rates reduce bond prices, while high inflation erodes real returns, particularly for fixed-rate instruments. (Bank for International Settlements, 2025)
<br>
    <br>5.
From an accounting and process standpoint, government-backed bonds are recorded as Debt Securities on the issuer's balance sheet and as Fixed-Income Investments on investor balance sheets. Due to standardized issuance and deep secondary markets, these bonds offer high liquidity and transparent pricing. (Deloitte, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>International Monetary Fund (IMF). (2025). Sovereign Debt and Government Bonds. <a href="https://www.imf.org/sovereign-debt">https://www.imf.org/sovereign-debt</a>
<br>
    <br>World Bank. (2025). Public Debt Management and Government Securities. <a href="https://www.worldbank.org/publicdebt">https://www.worldbank.org/publicdebt</a>
<br>
    <br>U.S. Department of the Treasury. (2025). Treasury Securities Overview. <a href="https://www.treasurydirect.gov">https://www.treasurydirect.gov</a>
<br>
    <br>Bank for International Settlements (BIS). (2025). Global Fixed Income Markets. <a href="https://www.bis.org">https://www.bis.org</a>
<br>
    <br>Deloitte. (2025). Accounting for Government Debt Securities. <a href="https://www2.deloitte.com/government-bonds">https://www2.deloitte.com/government-bonds</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Issuer Authority - Sovereign or government-sponsored entity
<br>•   Statutory Authorization - Public debt legislation or mandate
<br>•   Offering Documentation - Prospectus or offering circular
<br>•   Auction or Syndication Process - Primary market issuance method
<br>•   Settlement & Custody - Central securities depository participation
<br>•   Disclosure & Reporting - Fiscal and debt transparency requirements
<br>•   Regulatory Compliance - Securities and public finance regulations
<br>•   Currency & Jurisdiction Terms - Governing law and denomination


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Offering Circular / Prospectus - Issuance terms and disclosures
<br>•   Debt Issuance Authorization - Legislative or executive approval
<br>•   Auction Rules or Syndicate Agreement - Distribution mechanics
<br>•   Fiscal Budget Documents - Government revenue and expenditure data
<br>•   Debt Management Strategy - Issuer's debt profile and objectives
<br>•   Payment & Settlement Instructions - Clearing and custody details
<br>•   Legal Opinions - Validity and enforceability confirmations
<br>•   Rating Agency Reports - Sovereign credit assessments

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def bondsgovernmentbackedfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Bonds<br>
    Government Backed</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What are government-backed bonds?</u></b><br>
    •Answer: Government-backed bonds are debt securities issued or guaranteed by a government, offering investors a high level of safety and predictable returns.
</p>

    <p><u><b>2. Who issues government-backed bonds?</u></b><br>
    •Answer: These bonds are issued by national governments, state or municipal authorities, or government-sponsored entities.
</p>

    <p><u><b>3. Why do governments issue bonds?</u></b><br>
    •Answer: Governments issue bonds to finance public spending, infrastructure projects, budget deficits, and economic development initiatives.
</p>

    <p><u><b>4. How do government-backed bonds work?</u></b><br>
    •Answer: Investors lend money to the government in exchange for periodic interest payments and repayment of principal at maturity.
</p>

    <p><u><b>5. What types of government-backed bonds exist?</u></b><br>
    •Answer: Common types include treasury bonds, treasury bills, treasury notes, municipal bonds, and sovereign bonds.
</p>

    <p><u><b>6. What is the typical maturity of government-backed bonds?</u></b><br>
    •Answer: Maturities can range from short-term (less than 1 year) to long-term (10-30 years or more).
</p>

    <p><u><b>7. How are interest rates determined for government-backed bonds?</u></b><br>
    •Answer: Interest rates are influenced by central bank policy, inflation expectations, credit ratings, and overall market conditions.
</p>

    <p><u><b>8. Are government-backed bonds considered low risk?</u></b><br>
    •Answer: Yes, they are generally considered low-risk due to government backing, though risk levels vary by country.
</p>

    <p><u><b>9. Do government-backed bonds pay regular interest?</u></b><br>
    •Answer: Yes, most government-backed bonds pay fixed or variable interest (coupons) at regular intervals.
</p>

    <p><u><b>10. Can government-backed bonds be traded?</u></b><br>
    •Answer: Yes, most government-backed bonds are tradable in secondary markets before maturity.
</p>

    <p><u><b>11. Are government-backed bonds taxable?</u></b><br>
    •Answer: Tax treatment varies by jurisdiction; some government bonds offer tax exemptions or preferential tax treatment.
</p>

    <p><u><b>12. What are the benefits of investing in government-backed bonds?</u></b><br>
    •Answer: Benefits include capital preservation, stable income, high liquidity, and diversification.
</p>

    <p><u><b>13. What are the risks associated with government-backed bonds?</u></b><br>
    •Answer: Risks include interest rate risk, inflation risk, and sovereign credit risk in some countries.
</p>

    <p><u><b>14. How do government-backed bonds differ from corporate bonds?</u></b><br>
    •Answer: Government-backed bonds generally offer lower yields but higher safety compared to corporate bonds.
</p>

    <p><u><b>15. When should investors consider government-backed bonds?</u></b><br>
    •Answer: Investors should consider them when seeking low-risk investments, steady income, or portfolio stability.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def bondsgovernmentbackedtwelve(request):
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
    Capital Type: Government Backed</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Government-backed bonds are best suited for established entities with stable operations, predictable cash flows, and long-term funding needs. These instruments are typically used by mature companies, infrastructure projects, public-private partnerships, or special-purpose entities rather than early-stage startups, as they require demonstrated operating history and financial stability.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Eligible issuers are generally C-Corporations, government-linked entities, municipalities, or special purpose vehicles structured to meet program requirements. LLCs may qualify in certain jurisdictions, but sole proprietorships are generally not suitable due to regulatory, disclosure, and scale requirements associated with bond issuance.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Issuers of government-backed bonds typically have significant prior capital, established balance sheets, and a track record of servicing debt. While equity capitalization strengthens eligibility, underwriting is driven by creditworthiness, project viability, and government support mechanisms rather than venture-style funding history.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Government-backed bonds operate within the public and quasi-public fixed income markets and are supported by government guarantees, insurance programs, or agency backing. These bonds are often issued under national, regional, or multilateral government programs designed to promote infrastructure, housing, exports, or economic development.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Capital raised through government-backed bond issuances typically ranges from several million to billions of dollars, depending on project scale, issuer capacity, and program limits. The size of the issuance is driven by long-term capital requirements and market demand rather than startup-style funding needs.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Government-backed bonds are not capital rounds and do not involve equity issuance. They are structured as long-term debt instruments with defined maturities and repayment schedules, often aligned with the useful life of the underlying project or asset.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Bond proceeds are typically raised in a single issuance, though large programs may involve multiple tranches or series issued over time. Tranches may differ by maturity, interest rate, or repayment structure depending on investor demand and funding needs.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Funds raised through government-backed bonds are generally restricted to approved purposes such as infrastructure development, public services, housing, energy projects, export financing, or large-scale capital investments. Use of proceeds is closely monitored to ensure compliance with government program requirements.
<br>•   Infrastructure development and public services
<br>•   Housing and energy projects
<br>•   Export financing
<br>•   Large-scale capital investments

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk to investors is relatively low due to government guarantees or backing, though market, interest rate, and sovereign risk may still apply. For issuers, risk includes long-term repayment obligations, compliance with program covenants, and exposure to changes in government policy or funding support.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital is generally lower than unsecured or private debt due to government support, resulting in favorable interest rates and longer maturities. Costs include interest payments, underwriting fees, and ongoing compliance expenses, but are typically lower than comparable non-backed bonds.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are high and include legal structuring, regulatory approvals, underwriting fees, ratings assessments, disclosure documentation, and issuance expenses. These costs are justified by the large capital amounts and long-term financing benefits.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital is relatively long due to regulatory approvals, government coordination, and market issuance processes. The full timeline commonly ranges from several months to over a year, depending on jurisdiction, program complexity, and market conditions.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
