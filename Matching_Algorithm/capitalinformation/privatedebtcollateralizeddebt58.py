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
def privatedebtcollateralizeddebt(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Debt</b></u><br>
    Capital Type: Collateralized Debt </center></p>
    <p><b><u>Introduction</u></b><br>
Collateralized Debt is ideal for borrowers seeking debt financing supported by pledged assets to reduce lender risk and improve access to capital. It is designed so that loans are extended with specific collateral—such as real estate, equipment, receivables, inventory, or financial assets—providing lenders with enforceable security interests in the event of default. {n} fits that definition. In 2026, collateralized debt remains a cornerstone of private lending markets, widely used by operating companies, project sponsors, and special-purpose vehicles. Private credit funds and non-bank lenders frequently structure collateralized facilities to balance borrower flexibility with strong downside protection, particularly in asset-heavy or transitional businesses. While collateralized debt lowers borrowing costs relative to unsecured debt, it introduces asset encumbrance, valuation, and enforcement risk. Borrowers must manage covenants, collateral maintenance requirements, and potential loss of critical assets if performance deteriorates.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.Collateralized Debt is a form of private borrowing in which a lender extends credit secured by specific assets pledged by the borrower, granting the lender priority claims over the collateral in the event of default. (Corporate Finance Institute, 2026)
<br>


    <br>2.  Collateralized debt occupies a senior position within the Capital Stack, typically ranking ahead of unsecured debt and equity. Recovery outcomes depend on collateral quality, lien priority, and enforceability under applicable law. (Moody's Investors Service, 2025)
<br>

    <br>3. Legally, collateralized debt is governed by a Credit Agreement and perfected through security documents such as mortgages, pledges, or security agreements that establish liens over the pledged assets. These interests are often registered through UCC or equivalent filings. (Latham & Watkins, 2025)
<br>

    <br>4.From a risk perspective, collateralized debt shifts risk mitigation toward asset value and liquidity, exposing lenders and borrowers to valuation volatility, concentration risk, and enforcement complexity. Borrowers face the risk of asset seizure if covenants or repayment terms are breached. (S&P Global Ratings, 2025)
<br>

    <br>5.
From an accounting and process standpoint, collateralized debt is recorded as Secured Liabilities, with interest expense recognized over the loan term. The underwriting process emphasizes collateral appraisal, legal due diligence, and ongoing monitoring, often resulting in faster approvals than unsecured lending. (Deloitte, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Corporate Finance Institute (CFI). (2026). Secured and Collateralized Debt Financing. <a href="https://corporatefinanceinstitute.com/resources/credit-analysis">https://corporatefinanceinstitute.com/resources/credit-analysis</a>
<br>

    <br>Moody's Investors Service. (2025). Secured Lending and Recovery Analysis. <a href="https://www.moodys.com/secured-lending">https://www.moodys.com/secured-lending</a>
<br>

    <br>Latham & Watkins. (2025). Security Interests and Collateral Structures. <a href="https://www.lw.com/secured-finance">https://www.lw.com/secured-finance</a>
<br>

    <br>S&P Global Ratings. (2025). Collateral and Credit Risk Assessment. <a href="https://www.spglobal.com/ratings">https://www.spglobal.com/ratings</a>
<br>

    <br>Deloitte. (2025). Accounting for Secured Debt Instruments. <a href="https://www2.deloitte.com/secured-debt">https://www2.deloitte.com/secured-debt</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Borrower Eligibility – Operating company, SPV, or asset owner
<br>•   Defined Collateral – Real estate, equipment, receivables, inventory, or securities
<br>•   Collateral Valuation – Independent appraisal or valuation
<br>•   Security Documentation – Mortgage, pledge, or security agreement
<br>•   Lien Perfection – UCC or equivalent filings
<br>•   Financial & Maintenance Covenants – Leverage and asset coverage tests
<br>•   Insurance Requirements – Coverage on pledged assets
<br>•   Regulatory Compliance – Commercial lending and securities laws


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Credit Agreement – Primary loan contract
<br>•   Security Agreement – Collateral pledge terms
<br>•   Mortgage or Deed of Trust – Real estate security (if applicable)
<br>•   UCC Filings – Lien perfection documentation
<br>•   Appraisal Reports – Asset valuation
<br>•   Insurance Certificates – Coverage confirmation
<br>•   Financial Statements – Borrower financials
<br>•   Board Resolutions – Authorization to incur secured debt

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def privatedebtcollateralizeddebtfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Debt<br>
    Collateralized Debt</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is collateralized private debt?</u></b><br>
    •Answer: Collateralized private debt is a form of financing where a borrower receives capital secured by specific assets pledged as collateral.
</p>

    <p><u><b>2. Who provides collateralized private debt?</u></b><br>
    •Answer: It is typically provided by private lenders, private credit funds, NBFCs, hedge funds, or institutional investors.
</p>

    <p><u><b>3. When is collateralized private debt typically used?</u></b><br>
    •Answer: It is used when borrowers seek financing at lower interest rates than unsecured debt by offering assets as security.
</p>

    <p><u><b>4. How does collateralized private debt work?</u></b><br>
    •Answer: The borrower pledges assets as collateral, receives funding, and repays principal and interest under agreed terms, with lenders having claim to the collateral in case of default.
</p>

    <p><u><b>5. What types of assets can be used as collateral?</u></b><br>
    •Answer: Common collateral includes real estate, equipment, inventory, receivables, securities, or other tangible and financial assets.
</p>

    <p><u><b>6. How is loan value determined in collateralized private debt?</u></b><br>
    •Answer: Loan amounts are based on collateral value, typically using a loan-to-value (LTV) ratio set by the lender.
</p>

    <p><u><b>7. Are interest rates lower for collateralized private debt?</u></b><br>
    •Answer: Yes, rates are generally lower than unsecured private debt due to reduced lender risk.
</p>

    <p><u><b>8. What is the typical tenure of collateralized private debt?</u></b><br>
    •Answer: Tenure can range from short-term (1–3 years) to medium-term (3–7 years), depending on structure.
</p>

    <p><u><b>9. What happens if the borrower defaults?</u></b><br>
    •Answer: The lender has the right to seize or liquidate the collateral to recover outstanding amounts.
</p>

    <p><u><b>10. Are covenants common in collateralized private debt?</u></b><br>
    •Answer: Yes, covenants often include asset maintenance, financial ratios, reporting requirements, and usage restrictions.
</p>

    <p><u><b>11. What are the benefits of collateralized private debt for borrowers?</u></b><br>
    •Answer: Benefits include access to larger loan amounts, lower interest rates, and flexible structuring.
</p>

    <p><u><b>12. What are the risks of collateralized private debt?</u></b><br>
    •Answer: Risks include loss of pledged assets, restrictive covenants, and refinancing risk.
</p>

    <p><u><b>13. How does collateralized private debt differ from unsecured private debt?</u></b><br>
    •Answer: Collateralized debt is backed by assets and carries lower risk and cost, while unsecured debt relies solely on borrower creditworthiness.
</p>

    <p><u><b>14. Can collateralized private debt be used alongside other financing?</u></b><br>
    •Answer: Yes, it can be layered with equity, mezzanine debt, or other credit facilities subject to intercreditor agreements.
</p>

    <p><u><b>15. When should a borrower consider collateralized private debt?</u></b><br>
    •Answer: A borrower should consider it when they have valuable assets to pledge and want lower-cost private financing.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def privatedebtcollateralizeddebttwelve(request):
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
    Capital Type: Collateralized Debt</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Collateralized private debt is best suited for companies at early revenue through mature stages that possess tangible or clearly valued assets capable of being pledged as security. This form of financing is less dependent on company age and more reliant on asset quality, making it viable for businesses that may not qualify for unsecured or cash-flow–based lending.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
C-Corporations and LLCs are the preferred entity types for collateralized debt, as they provide clear asset ownership, enforceable security interests, and standardized legal structures. Sole proprietorships may qualify in limited cases but are generally less favored due to weaker legal separation between the borrower and pledged assets.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Collateralized debt can be accessed by companies with limited or significant prior capital, as underwriting is primarily based on the value, liquidity, and enforceability of the collateral rather than the company's capitalization or fundraising history. Existing equity or debt does not preclude eligibility if sufficient collateral is available.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Collateralized private debt operates within the private credit and asset-based lending market and is typically provided by private lenders, family offices, private credit funds, and non-bank financial institutions. This market prioritizes security and downside protection over growth upside.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
The amount of capital available through collateralized debt is driven by loan-to-value ratios and the market value of the pledged assets. Loan sizes can range from tens of thousands to tens of millions of dollars, depending on asset type, liquidity, and lender risk tolerance.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Collateralized debt is not considered a capital round and does not involve equity issuance. It is structured as a standalone debt facility secured by specific assets and may be used as bridge financing, growth capital, or refinancing capital.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds are commonly disbursed in a single tranche at closing. In certain cases, staged disbursements may be used when the loan supports asset acquisition, development, or phased capital deployment, with releases tied to predefined milestones.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Proceeds from collateralized debt are typically used for asset acquisition, expansion, refinancing existing obligations, working capital, or liquidity needs. Use of funds may be restricted to purposes aligned with the collateral or lender requirements.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk to lenders is mitigated by the pledged collateral but remains subject to asset valuation risk, liquidity risk, and enforcement complexity. For borrowers, risk includes asset seizure in the event of default, restrictive covenants, and limited flexibility due to collateral constraints.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital for collateralized debt is generally lower than unsecured private debt due to reduced lender risk, but higher than traditional bank financing. Costs include interest payments, origination fees, and sometimes collateral monitoring or maintenance expenses.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are moderate and may include legal documentation, collateral valuation or appraisal fees, lien filings, and due diligence expenses. Costs increase with complex asset structures or multiple collateral types.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital is faster than traditional bank lending but slower than unsecured alternative financing, typically ranging from two to six weeks depending on collateral valuation, documentation, and lender diligence requirements.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
