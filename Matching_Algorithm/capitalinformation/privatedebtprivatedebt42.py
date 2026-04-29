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
def privatedebtprivatedebt(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Debt</b></u><br>
    Capital Type: Private Debt </center></p>
    <p><b><u>Introduction</u></b><br>
Private Debt is ideal for mid-market companies and established startups that require more capital or more flexible terms than traditional commercial banks can provide, but do not wish to dilute ownership through equity. It is designed so that non-bank financial institutions—such as debt funds, insurance companies, and BDCs (Business Development Companies)—can provide tailored loan structures for acquisitions, expansion, or recapitalization. {n} fits that definition. Private Debt has evolved from a niche alternative into a powerhouse of the global financial system. In 2026, the global private debt market is projected to exceed $2.3 trillion in assets under management. As commercial banks face tightening capital requirements, private lenders like Ares, HPS Investment Partners, and Blue Owl have become the primary source of "stretched" senior debt and untrenched facilities. On average, private debt deals range from $5 million to over $250 million, with interest rates typically floating at 5% to 8% above SOFR, reflecting a premium for the speed and flexibility they offer. While Private Debt provides "one-stop shop" financing solutions with fewer amortizing requirements, the primary risks include higher interest costs and "strict" maintenance covenants that, if breached, give the lender significant control over the company's strategic direction.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.Private Debt (also known as Direct Lending) refers to any debt that is not provided by a bank and is not traded on a public exchange (like a corporate bond). These loans are typically "Senior Secured," meaning they have a first-priority claim on assets. Unlike a bank loan that might be sold to other investors (syndicated), private debt is usually "buy-and-hold," where the lender maintains a direct, long-term relationship with the borrower. (Investopedia, 2026)
<br>


    <br>2.  The best type of companies to raise private debt are those with "Strong EBITDA" (Earnings Before Interest, Taxes, Depreciation, and Amortization) but high leverage needs that exceed bank limits. It is particularly effective for Private Equity-backed companies undergoing a "Leveraged Buyout" (LBO) or independent "Middle Market" firms looking to acquire a competitor without giving up a board seat to an equity partner. (Preqin, 2025)
<br>

    <br>3. Private Debt emerged as a dominant asset class following the 2008 financial crisis (the "Great Financial Crisis"). Regulations like the Dodd-Frank Act made it difficult for banks to hold "leveraged" loans on their balance sheets, creating a vacuum that private funds filled. In 2025 and 2026, the market has matured with the rise of "Unitranche" financing, which blends senior and junior debt into a single loan with a single interest rate, simplifying the capital structure for the founder. (BlackRock, 2025)
<br>

    <br>4.While Private Debt offers speed, it carries "Variable Rate and Covenant" risks. Because most private debt is floating-rate, a sudden rise in market interest rates can dramatically increase debt service costs. Furthermore, many deals include "Incurrence Covenants" or "Maintenance Covenants" (e.g., Debt/EBITDA ratios). If a company's performance dips, the lender can charge "Default Interest" or even force a change in management. (Goldman Sachs Asset Management, 2025)
<br>

    <br>5.
To raise private debt, a company must undergo a "Quality of Earnings" (QofE) review. Lenders focus heavily on "Cash Flow Conversion"—how much of the profit actually turns into cash to pay interest. The process is faster than a public bond offering but more intensive than a small bank loan. Success requires a sophisticated financial team capable of managing the ongoing reporting and compliance required by institutional debt funds. (Morgan Stanley, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Investopedia.. Investopedia. (2026, Jan 03). Private Debt: What It Is and How It Works.. <a href="https://www.investopedia.com/terms/p/private-debt.asp">https://www.investopedia.com/terms/p/private-debt.asp</a>
<br>

    <br>Preqin. (2025). 2025 Global Private Debt Report: Trends and Outlook. <a href="https://www.preqin.com/insights/global-reports/2025-preqin-global-private-debt-report">https://www.preqin.com/insights/global-reports/2025-preqin-global-private-debt-report</a>
<br>

    <br>BlackRock.. BlackRock. (2025, Sept 12). The Rise of Direct Lending in the Middle Market.. <a href="https://www.blackrock.com/institutions/en-us/insights/private-debt-outlook">https://www.blackrock.com/institutions/en-us/insights/private-debt-outlook</a>
<br>

    <br>Goldman Sachs Asset Management. (2025). Private Credit: Navigating Covenants and Rates. <a href="https://www.gsam.com/content/gsam/us/en/institutions/market-insights.html">https://www.gsam.com/content/gsam/us/en/institutions/market-insights.html</a>
<br>

    <br>Morgan Stanley.. Morgan Stanley. (2025, Nov 20). Why Companies are Choosing Private Debt Over Public Markets.. <a href="https://www.morganstanley.com/ideas/private-credit-growth-2025">https://www.morganstanley.com/ideas/private-credit-growth-2025</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Accredited Borrower Status – Generally reserved for established entities with a clear corporate structure (LLC or C-Corp).
<br>•   Solvency Requirements – The borrower must demonstrate they are not insolvent at the time of the loan.
<br>•   First-Priority Security Interest – Lenders will require a UCC-1 filing and often a "control agreement" over bank accounts.
<br>•   Compliance with "Negative Covenants" – Legal restrictions on the company's ability to sell assets, pay dividends, or take on other debt.
<br>•   Intercreditor Agreements – If multiple lenders are involved, a legal contract must define the "waterfall" of who gets paid first.
<br>•   Anti-Money Laundering (AML) / KYC – Extensive background checks on all "Beneficial Owners" (those with >25% ownership).


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Quality of Earnings (QofE) Report – A detailed third-party audit of historical cash flows.
<br>•   Credit Agreement – The primary legal contract (often 100+ pages) governing the loan.
<br>•   Financial Model – Monthly or quarterly projections for the next 3–5 years.
<br>•   Capitalization Table – Showing the full ownership structure.
<br>•   UCC-1 Filing – Evidence of the lender's lien on all business assets.
<br>•   Disclosure Schedules – A list of all existing litigation, contracts, and liabilities.
<br>•   Organizational Chart – Visualizing all subsidiaries and parent entities.

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def privatedebtprivatedebtfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Debt<br>
    Private Debt</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is private debt?</u></b><br>
    •Answer: Private debt refers to non-publicly traded loans provided by private lenders, such as private funds, institutions, or high-net-worth individuals, to businesses or projects.
</p>

    <p><u><b>2. How does private debt differ from public debt?</u></b><br>
    •Answer: Private debt is negotiated directly between lender and borrower, while public debt is issued in public markets through bonds or debentures.
</p>

    <p><u><b>3. Who provides private debt financing?</u></b><br>
    •Answer: Private debt is provided by private credit funds, hedge funds, insurance companies, pension funds, family offices, and wealthy individuals.
</p>

    <p><u><b>4. Who typically uses private debt?</u></b><br>
    •Answer: Mid-market companies, startups, growing businesses, and firms with limited access to traditional bank financing commonly use private debt.
</p>

    <p><u><b>5. What are the common types of private debt?</u></b><br>
    •Answer: Common types include senior secured loans, mezzanine debt, subordinated debt, bridge loans, and asset-based lending.
</p>

    <p><u><b>6. Is private debt secured or unsecured?</u></b><br>
    •Answer: Private debt can be either secured by assets or unsecured, depending on the risk profile and negotiated terms.
</p>

    <p><u><b>7. What are the advantages of private debt?</u></b><br>
    •Answer: Advantages include flexible terms, faster execution, customized structures, and access to capital when banks are restrictive.
</p>

    <p><u><b>8. What are the disadvantages of private debt?</u></b><br>
    •Answer: Disadvantages include higher interest rates, stricter covenants, and greater lender control compared to traditional loans.
</p>

    <p><u><b>9. How are interest rates determined in private debt?</u></b><br>
    •Answer: Interest rates are based on borrower risk, collateral quality, loan structure, market conditions, and lender return requirements.
</p>

    <p><u><b>10. What is the typical maturity of private debt?</u></b><br>
    •Answer: Maturities vary widely, ranging from short-term bridge loans to long-term financing lasting five to ten years.
</p>

    <p><u><b>11. Can private debt be used for acquisitions?</u></b><br>
    •Answer: Yes, private debt is commonly used in mergers, acquisitions, leveraged buyouts, and expansion strategies.
</p>

    <p><u><b>12. Is private debt suitable for startups?</u></b><br>
    •Answer: It may be suitable for later-stage startups with stable cash flows or assets, but early-stage startups typically rely more on equity.
</p>

    <p><u><b>13. How does private debt affect ownership?</u></b><br>
    •Answer: Private debt does not dilute ownership, but lenders may impose covenants or rights that influence business decisions.
</p>

    <p><u><b>14. What risks do borrowers face with private debt?</u></b><br>
    •Answer: Risks include repayment pressure, covenant breaches, refinancing risk, and potential loss of collateral upon default.
</p>

    <p><u><b>15. Why is private debt growing in popularity?</u></b><br>
    •Answer: Private debt is growing due to tighter bank regulations, demand for flexible financing, and investors seeking higher yields.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def privatedebtprivatedebttwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Private Debt</b></u><br>
    Capital Type: Private Debt</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Private debt is best suited for operating businesses across growth-stage to mature-stage, including companies that may not fully meet traditional bank lending criteria. It is also used by later-stage startups with predictable cash flows.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Private debt is commonly available to C-Corps, LLCs, and S-Corps. Lenders prefer entities with clear governance structures, enforceable contracts, and defined ownership. Sole proprietorships are less common unless supported by strong personal guarantees.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Businesses may already have existing debt or equity financing, but lenders will closely assess leverage levels, repayment capacity, and cash flow stability. Private lenders are generally more flexible than banks but still require financial transparency.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Private debt operates in the private credit market, with capital provided by private credit funds, hedge funds, family offices, and specialty lenders rather than regulated commercial banks.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Private debt facilities typically range from $500,000 to tens of millions of dollars, depending on company size, collateral availability, and risk profile. Loan size is often structured to complement existing capital.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Private debt is not an equity capital round. It is often layered alongside equity raises or used as an alternative to bank financing to avoid ownership dilution.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funding may be structured as a single disbursement, multiple tranches, or a revolving facility, depending on the lender and the borrower's cash flow needs.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Permitted uses generally include:
<br>•   Working capital
<br>•   Growth initiatives
<br>•   Refinancing existing debt
<br>•   Acquisitions or expansion
Restrictions usually prohibit personal use, speculative investments, or activities outside the company's core operations.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk is moderate to high, depending on leverage, collateral strength, and repayment structure. Borrowers face covenant risk and refinancing risk, while lenders mitigate exposure through pricing and collateral.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of private debt is higher than traditional bank loans due to increased risk tolerance. Pricing includes higher interest rates, lender fees, and sometimes performance-based returns.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are moderate, including legal fees, due diligence expenses, origination fees, and potential collateral valuation costs.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital is relatively fast, typically 3–8 weeks, depending on complexity, underwriting requirements, and negotiation of terms.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)