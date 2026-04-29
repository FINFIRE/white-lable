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

def bondshighyieldjunk(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Bonds</b></u><br>
    Capital Type: High Yield Junk </center></p>
    <p><b><u>Introduction</u></b><br>
High Yield (Junk) Bonds are ideal for investors seeking enhanced returns in exchange for accepting elevated credit risk. They are designed so that capital is raised by issuers with lower credit ratings or higher leverage profiles, offering higher coupon rates to compensate investors for increased default and volatility risk. {n} fits that definition. In 2026, the high-yield bond market remains a critical financing channel for leveraged companies, private equity-backed issuers, and firms undergoing restructuring or rapid growth. These bonds are widely used to fund acquisitions, recapitalizations, refinancings, and expansion initiatives, particularly in capital-intensive and cyclical industries. While high-yield bonds offer attractive income potential, they are exposed to credit deterioration, refinancing risk, and economic sensitivity. Changes in interest rates, tightening credit conditions, or issuer-specific underperformance can materially impact bond prices and recovery outcomes.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.A High Yield (Junk) Bond is a corporate debt security issued by an entity with a below-investment-grade credit rating (typically BB+ or lower) or with no rating, offering higher interest payments to compensate investors for increased credit and default risk. (Moody's Investors Service, 2025)
<br>


    <br>2.  High-yield bonds occupy a subordinate position within the Capital Stack relative to investment-grade and senior secured debt, though they typically rank ahead of equity. Recovery in default depends on seniority, collateral, and intercreditor arrangements. (S&P Global Ratings, 2025)
<br>

    <br>3. Legally, high-yield bonds are governed by an Indenture Agreement that outlines coupon rates, maturity, covenants, call provisions, and events of default. Issuances are typically marketed via offering memoranda and sold through private placements or public offerings. (Latham & Watkins, 2025)
<br>
    <br>4.From a risk perspective, high-yield bonds expose investors to heightened default, downgrade, and refinancing risk, particularly during economic downturns. Issuers may face limited access to capital markets if credit conditions tighten, increasing rollover risk at maturity. (Bank for International Settlements, 2025)
<br>
    <br>5.
From an accounting and process standpoint, high-yield bonds are recorded as Long-Term Debt on the issuer's balance sheet, with interest expense recognized over time. Due to active secondary markets, these bonds offer tradability but experience greater price volatility than investment-grade securities. (Deloitte, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Moody's Investors Service. (2025). High-Yield Bond Market Outlook. <a href="https://www.moodys.com/high-yield">https://www.moodys.com/high-yield</a>
<br>
    <br>S&P Global Ratings. (2025). Credit Risk in Speculative-Grade Debt. <a href="https://www.spglobal.com/ratings">https://www.spglobal.com/ratings</a>
<br>
    <br>Latham & Watkins. (2025). High-Yield Bond Issuance Structures. <a href="https://www.lw.com/high-yield">https://www.lw.com/high-yield</a>
<br>
    <br>Bank for International Settlements (BIS). (2025). Corporate Credit Cycles and Risk. <a href="https://www.bis.org">https://www.bis.org</a>
<br>
    <br>Deloitte. (2025). Accounting for Corporate Debt Securities. <a href="https://www2.deloitte.com/corporate-debt">https://www2.deloitte.com/corporate-debt</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Issuer Eligibility - Below-investment-grade or unrated entity
<br>•   Credit Disclosure - Risk factors and financial disclosures
<br>•   Indenture Covenants - Leverage, restricted payments, and incurrence tests
<br>•   Offering Structure - Public or private placement compliance
<br>•   Rating Agency Engagement - Credit assessment and monitoring
<br>•   Regulatory Compliance - Securities and disclosure regulations
<br>•   Change-of-Control Provisions - Investor protection clauses
<br>•   Redemption & Call Terms - Early repayment conditions


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Offering Memorandum / Prospectus - Issuance disclosures
<br>•   Indenture Agreement - Bondholder rights and covenants
<br>•   Credit Rating Reports - Rating agency assessments
<br>•   Financial Statements - Historical and projected performance
<br>•   Use-of-Proceeds Statement - Capital deployment plan
<br>•   Legal Opinions - Validity and enforceability confirmations
<br>•   Trustee Agreement - Bond administration and oversight
<br>•   Board Resolutions - Authorization to issue bonds

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def bondshighyieldjunkfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Bonds<br>
    High Yield Junk</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What are high-yield (junk) bonds?</u></b><br>
    •Answer: High-yield bonds, commonly known as junk bonds, are corporate debt securities issued by companies with lower credit ratings and higher default risk.
</p>

    <p><u><b>2. Who issues high-yield bonds?</u></b><br>
    •Answer: High-yield bonds are issued by companies with below-investment-grade credit ratings or by companies seeking capital without traditional bank financing.
</p>

    <p><u><b>3. When are high-yield bonds typically used?</u></b><br>
    •Answer: They are used by companies to finance growth, acquisitions, restructuring, or refinancing when lower-cost debt is unavailable.
</p>

    <p><u><b>4. How do high-yield bonds work?</u></b><br>
    •Answer: Investors lend money to the issuer in exchange for higher interest payments and repayment of principal at maturity.
</p>

    <p><u><b>5. What credit ratings define high-yield bonds?</u></b><br>
    •Answer: Bonds rated below BBB- by S&P/Fitch or below Baa3 by Moody's are considered high-yield.
</p>

    <p><u><b>6. Why do high-yield bonds offer higher interest rates?</u></b><br>
    •Answer: Higher interest compensates investors for increased credit and default risk.
</p>

    <p><u><b>7. What is the typical maturity of high-yield bonds?</u></b><br>
    •Answer: Maturities usually range from 5 to 10 years.
</p>

    <p><u><b>8. Are high-yield bonds secured or unsecured?</u></b><br>
    •Answer: They can be either secured or unsecured, depending on the bond structure and issuer terms.
</p>

    <p><u><b>9. Do high-yield bonds pay regular interest?</u></b><br>
    •Answer: Yes, most pay fixed coupon interest at regular intervals.
</p>

    <p><u><b>10. Can high-yield bonds be traded in the market?</u></b><br>
    •Answer: Yes, high-yield bonds are traded in secondary markets, though liquidity may be lower than investment-grade bonds.
</p>

    <p><u><b>11. What are the benefits of investing in high-yield bonds?</u></b><br>
    •Answer: Benefits include higher income potential and portfolio yield enhancement.
</p>

    <p><u><b>12. What risks are associated with high-yield bonds?</u></b><br>
    •Answer: Risks include higher default risk, credit rating downgrades, price volatility, and economic sensitivity.
</p>

    <p><u><b>13. How do high-yield bonds differ from investment-grade bonds?</u></b><br>
    •Answer: High-yield bonds offer higher returns but carry greater risk compared to investment-grade bonds.
</p>

    <p><u><b>14. How do high-yield bonds perform during economic downturns?</u></b><br>
    •Answer: They often underperform due to increased default risk and reduced investor risk appetite.
</p>

    <p><u><b>15. When should investors consider high-yield bonds?</u></b><br>
    •Answer: Investors should consider them when seeking higher returns, can tolerate risk, and want income diversification within a broader portfolio.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def bondshighyieldjunktwelve(request):
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
    Capital Type: High Yield Junk</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
High yield bonds are best suited for late-stage or mature companies that have established operating history and meaningful revenue but do not meet investment-grade credit standards. These instruments are not appropriate for early-stage startups and are typically used by companies with scale, leverage, or transitional risk profiles seeking access to large pools of capital.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Issuers of high yield bonds are typically C-Corporations or large operating entities with the legal, financial, and reporting infrastructure required for public or private bond issuance. LLCs may issue in certain cases, but sole proprietorships are not suitable due to disclosure, scale, and regulatory requirements.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Companies issuing high yield bonds usually have significant prior capitalization, including equity investment and existing debt. While leverage may already be elevated, issuers must demonstrate sufficient cash flow to service interest payments. Credit history, debt structure, and refinancing strategy are critical underwriting considerations.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
High yield bonds operate within the public and private capital markets, primarily in the sub-investment-grade fixed income segment. Investors include institutional asset managers, hedge funds, private credit funds, and specialized high yield bond investors seeking higher returns in exchange for increased risk.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Capital raised through high yield bond issuances typically ranges from tens of millions to several billion dollars, depending on issuer size, market conditions, and investor demand. Issuance size is driven by refinancing needs, acquisitions, leveraged recapitalizations, or large-scale growth initiatives.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
High yield bonds are not considered capital rounds and do not involve equity issuance. They are structured as long-term or medium-term debt instruments with fixed or floating interest rates, defined maturities, and covenant packages negotiated with investors.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Bond offerings may be issued as a single tranche or multiple tranches with varying maturities, coupon rates, or seniority. Multi-tranche structures are common when issuers seek to optimize pricing and broaden investor participation.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Proceeds from high yield bonds are commonly used for refinancing existing debt, funding acquisitions, leveraged buyouts, dividends, share repurchases, or major capital expenditures. Use of funds is typically disclosed in offering materials but less restricted than government-backed bonds.
<br>•   Refinancing existing debt and recapitalizations
<br>•   Funding acquisitions and leveraged buyouts
<br>•   Dividends and share repurchases
<br>•   Major capital expenditures

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Investor risk is high due to elevated default probability, credit volatility, and sensitivity to economic conditions. Issuers face refinancing risk, covenant pressure, and higher scrutiny from markets, particularly during downturns or periods of rising interest rates.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital is high relative to investment-grade bonds and bank debt, reflecting increased credit risk. Costs include higher coupon rates, original issue discounts, and underwriting fees, resulting in a materially higher overall cost of borrowing.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are significant and include legal and disclosure documentation, underwriting and placement fees, ratings assessments, and advisory expenses. These costs are typically justified by the large size and strategic importance of the capital raised.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital depends on market conditions and issuer readiness but typically ranges from several weeks to a few months. Issuance windows can open and close quickly based on investor sentiment and macroeconomic factors.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
