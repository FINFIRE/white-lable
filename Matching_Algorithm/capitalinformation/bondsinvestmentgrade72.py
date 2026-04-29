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

def bondsinvestmentgrade(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Bonds</b></u><br>
    Capital Type: Investment Grade </center></p>
    <p><b><u>Introduction</u></b><br>
Investment Grade Bonds are ideal for investors seeking stable income and lower credit risk relative to speculative-grade debt. They are designed so that capital is raised by issuers with strong credit profiles—typically governments, supranational entities, or financially stable corporations—offering predictable interest payments and principal repayment. {n} fits that definition. In 2026, investment grade bonds remain a core component of global fixed-income portfolios, widely used by institutional investors, pension funds, insurers, and conservative asset allocators. These bonds serve as benchmarks for credit spreads and are commonly issued to finance capital expenditures, refinancing, and balance-sheet optimization. While investment grade bonds offer lower default risk, they are exposed to interest rate risk, duration risk, and spread widening. Changes in monetary policy or issuer fundamentals can affect market value, particularly for longer-dated securities.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.An Investment Grade Bond is a debt security issued by an entity with a credit rating of BBB-/Baa3 or higher from a recognized rating agency, indicating a relatively low probability of default and strong capacity to meet financial obligations. (Moody's Investors Service, 2025)
<br>


    <br>2.  Investment grade bonds occupy a senior position within the Capital Stack, typically ranking ahead of subordinated debt and equity. Recovery prospects in default scenarios are generally higher than for speculative-grade instruments. (S&P Global Ratings, 2025)
<br>

    <br>3. Legally, investment grade bonds are governed by an Indenture Agreement and disclosed through a prospectus or offering memorandum that specifies coupon structure, maturity, covenants, and events of default. Issuance may be public or private. (Latham & Watkins, 2025)
<br>
    <br>4.From a risk perspective, investment grade bonds minimize credit risk but remain sensitive to interest rate movements, duration exposure, and credit spread changes. Downgrades can materially affect liquidity and pricing, particularly for bonds near the rating threshold. (Bank for International Settlements, 2025)
<br>
    <br>5.
From an accounting and process standpoint, investment grade bonds are recorded as Long-Term Debt by issuers and as Investment Securities by investors. Deep secondary markets provide liquidity, transparent pricing, and efficient settlement. (Deloitte, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Moody's Investors Service. (2025). Investment Grade Credit Ratings. <a href="https://www.moodys.com">https://www.moodys.com</a>
<br>
    <br>S&P Global Ratings. (2025). Corporate Credit Rating Definitions. <a href="https://www.spglobal.com/ratings">https://www.spglobal.com/ratings</a>
<br>
    <br>Latham & Watkins. (2025). Investment Grade Bond Issuance Framework. <a href="https://www.lw.com/capital-markets">https://www.lw.com/capital-markets</a>
<br>
    <br>Bank for International Settlements (BIS). (2025). Global Fixed-Income Risk Factors. <a href="https://www.bis.org">https://www.bis.org</a>
<br>
    <br>Deloitte. (2025). Accounting for Investment-Grade Debt Securities. <a href="https://www2.deloitte.com/debt-accounting">https://www2.deloitte.com/debt-accounting</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Issuer Credit Quality - Investment grade rating (BBB-/Baa3 or higher)
<br>•   Offering Documentation - Prospectus or offering memorandum
<br>•   Rating Agency Engagement - Initial rating and ongoing surveillance
<br>•   Regulatory Compliance - Securities laws and disclosure standards
<br>•   Covenant Structure - Financial and operational protections
<br>•   Listing Requirements - Exchange or OTC eligibility (if applicable)
<br>•   Settlement & Custody - Clearing through recognized depositories
<br>•   Ongoing Disclosure - Periodic financial reporting


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Offering Circular / Prospectus - Bond terms and disclosures
<br>•   Indenture Agreement - Bondholder rights and covenants
<br>•   Credit Rating Reports - Rating agency assessments
<br>•   Financial Statements - Issuer financial condition
<br>•   Use-of-Proceeds Statement - Capital allocation plan
<br>•   Legal Opinions - Validity and enforceability
<br>•   Trustee Agreement - Bond administration
<br>•   Board Resolutions - Authorization to issue bonds

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def bondsinvestmentgradefaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Bonds<br>
    Investment Grade</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What are investment-grade bonds?</u></b><br>
    •Answer: Investment-grade bonds are debt securities issued by governments or corporations with strong credit ratings, indicating low default risk.
</p>

    <p><u><b>2. Who issues investment-grade bonds?</u></b><br>
    •Answer: They are issued by financially stable corporations, governments, and government-backed entities.
</p>

    <p><u><b>3. How are investment-grade bonds rated?</u></b><br>
    •Answer: They are rated BBB- or higher by S&P and Fitch, or Baa3 or higher by Moody's.
</p>

    <p><u><b>4. When are investment-grade bonds typically used?</u></b><br>
    •Answer: Issuers use them to raise capital for operations, expansion, refinancing, or infrastructure projects.
</p>

    <p><u><b>5. How do investment-grade bonds work?</u></b><br>
    •Answer: Investors lend money to the issuer in exchange for regular interest payments and repayment of principal at maturity.
</p>

    <p><u><b>6. Do investment-grade bonds pay regular interest?</u></b><br>
    •Answer: Yes, they typically pay fixed or floating coupon interest at regular intervals.
</p>

    <p><u><b>7. What is the typical maturity of investment-grade bonds?</u></b><br>
    •Answer: Maturities can range from short-term (1-3 years) to long-term (10-30 years).
</p>

    <p><u><b>8. Are investment-grade bonds considered low risk?</u></b><br>
    •Answer: Yes, they are considered relatively low risk compared to high-yield bonds.
</p>

    <p><u><b>9. Can investment-grade bonds be traded in secondary markets?</u></b><br>
    •Answer: Yes, they are actively traded and generally more liquid than lower-rated bonds.
</p>

    <p><u><b>10. What are the benefits of investing in investment-grade bonds?</u></b><br>
    •Answer: Benefits include capital preservation, steady income, and portfolio stability.
</p>

    <p><u><b>11. What risks are associated with investment-grade bonds?</u></b><br>
    •Answer: Risks include interest rate risk, inflation risk, and credit rating downgrades.
</p>

    <p><u><b>12. How do investment-grade bonds differ from high-yield bonds?</u></b><br>
    •Answer: Investment-grade bonds have lower yields but significantly lower credit risk than high-yield bonds.
</p>

    <p><u><b>13. Who typically invests in investment-grade bonds?</u></b><br>
    •Answer: Institutional investors, pension funds, insurance companies, and conservative individual investors commonly invest in them.
</p>

    <p><u><b>14. Are investment-grade bonds suitable for conservative investors?</u></b><br>
    •Answer: Yes, they are well-suited for investors seeking lower risk and stable income.
</p>

    <p><u><b>15. When should investors consider investment-grade bonds?</u></b><br>
    •Answer: Investors should consider them when prioritizing safety, income stability, and long-term portfolio balance.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def bondsinvestmentgradetwelve(request):
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
    Capital Type: Investment Grade</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Investment grade bonds are best suited for mature companies with strong operating history, stable cash flows, and proven financial performance. These instruments are not appropriate for early-stage or growth-stage startups, as issuers must demonstrate consistent earnings, balance sheet strength, and the ability to service long-term debt at low risk.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Eligible issuers are typically C-Corporations, financial institutions, government-backed entities, or large operating companies with established governance and reporting standards. LLCs may qualify in certain structures, but sole proprietorships are not suitable due to regulatory, disclosure, and scale requirements.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Issuers of investment grade bonds generally have significant prior capitalization and existing debt and equity structures. Credit ratings, leverage ratios, cash flow coverage, and financial transparency are central to eligibility and pricing, rather than venture-style fundraising history.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Investment grade bonds operate within the public and institutional fixed income markets. Investors typically include pension funds, insurance companies, asset managers, and other conservative institutional investors seeking capital preservation and stable returns.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Capital raised through investment grade bond issuances typically ranges from hundreds of millions to several billion dollars, depending on issuer size, credit rating, and market conditions. Issuance size reflects long-term funding needs and market demand.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Investment grade bonds are not capital rounds and do not involve equity issuance. They are structured as long-term debt securities with defined maturities, coupon payments, and repayment schedules.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Bond offerings may be structured as a single tranche or multiple tranches with varying maturities and coupon rates. Multi-tranche issuances are common to optimize investor demand and manage interest rate exposure.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Proceeds are typically used for refinancing existing debt, funding capital expenditures, acquisitions, infrastructure investment, or general corporate purposes. Use of funds is disclosed but generally flexible.
<br>•   Refinancing existing debt
<br>•   Capital expenditures and infrastructure
<br>•   Acquisitions and expansion
<br>•   General corporate purposes

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Investor risk is relatively low due to strong credit quality, though interest rate risk and macroeconomic factors still apply. Issuers face long-term repayment obligations and exposure to changes in interest rates and credit market conditions.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital is low relative to other debt instruments and reflects favorable interest rates due to strong credit ratings. Costs include interest payments, underwriting spreads, and compliance expenses, but are among the most efficient forms of large-scale financing.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are high and include underwriting fees, legal and disclosure documentation, ratings agency fees, and regulatory compliance expenses. These costs are justified by the large capital amounts and long maturities.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital typically ranges from several weeks to a few months, depending on market conditions, issuer readiness, and regulatory requirements.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
