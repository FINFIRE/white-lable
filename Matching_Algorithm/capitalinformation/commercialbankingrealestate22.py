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

def commercialbankingrealestate(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Commercial Banking</b></u><br>
    Capital Type: Real Estate Loan </center></p>
    <p><b><u>Introduction</u></b><br>
Commercial Real Estate (CRE) Loans are ideal for companies seeking capital to purchase, develop, or refinance income-producing properties or owner-occupied business premises. They are designed so that financial institutions can provide long-term, asset-backed financing to help privately held businesses build equity in physical locations and secure operational stability. {n} fits that definition. Commercial real estate loans have been the backbone of urban development for over a century. In 2024, the total outstanding commercial mortgage debt in the United States exceeded $4.6 trillion, with major lenders like Wells Fargo and Goldman Sachs financing everything from medical offices to industrial warehouses. Unlike residential mortgages, CRE loans are primarily evaluated on the property's income-generating potential and the business's debt-service coverage. On average, CRE loan recipients gain access to between $250,000 and $5 million+, typically requiring a down payment of 20% to 35% and offering repayment terms ranging from 5 to 20 years. While real estate loans allow for wealth accumulation through appreciation, the risks of market volatility, significant upfront capital requirements, and "balloon payments" at the end of the term require sophisticated financial planning.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.A Commercial Real Estate Loan is a mortgage-backed security specifically for properties used for business purposes, such as retail centers, offices, hotels, or apartment complexes. These loans are secured by the property itself as collateral. Unlike residential loans, CRE loans are often made to business entities (e.g., LLCs or Corporations) rather than individuals, and the interest rates are typically higher due to the increased risk associated with business operations. (Investopedia, 2025)
<br>


    <br>2.  The best type of companies to raise capital via a CRE loan are those with stable, predictable cash flows and a need for permanent physical space or an investment in income-producing property. This includes professional service firms (doctors, lawyers), manufacturers requiring specialized plants, and real estate developers. Lenders look for a "Debt Service Coverage Ratio" (DSCR) of at least 1.2x, meaning the property or business generates 20% more income than is required to pay the debt. (Commercial Loan Direct, 2025)
<br>

    <br>3. Commercial Real Estate Loans emerged alongside the rise of the modern city in the late 19th century. The evolution of the "Life Insurance Company Loan" and the "CMBS" (Commercial Mortgage-Backed Security) market in the 1990s revolutionized the field by pooling loans into packages for investors. This shifted the market from simple local bank lending to a global capital market, significantly increasing the volume of available credit for large-scale developments. (The Balance, 2024)
<br>
    <br>4.While CRE loans build equity, they carry structural risks. Many commercial loans are not fully "amortized," meaning they don't pay off completely over the term. Instead, they often have a balloon payment—a large lump sum due at the end of 5 or 10 years—which requires the business to refinance or sell the property. Furthermore, if the property's value drops, the bank may issue a "margin call," requiring the borrower to provide additional cash to maintain the required Loan-to-Value (LTV) ratio. (Bankrate, 2025)
<br>
    <br>5.
To raise capital via a CRE loan, a company must undergo a rigorous "property-level" and "borrower-level" underwriting process. The bank will commission an independent appraisal to determine the fair market value and an environmental assessment (Phase I) to ensure the land isn't contaminated. Borrowers must provide detailed "rent rolls" if the property has tenants and a clear "Sources and Uses" statement showing how the loan proceeds and the down payment will be allocated. (J.P. Morgan Commercial Banking, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Investopedia. (2025). Commercial Real Estate Loan Definition and Types. <a href="https://www.investopedia.com/terms/c/commercial-real-estate-loan.asp">https://www.investopedia.com/terms/c/commercial-real-estate-loan.asp</a>
<br>
    <br>Commercial Loan Direct. (2025). Understanding the Debt Service Coverage Ratio (DSCR). <a href="https://www.commercialloandirect.com/dscr.html">https://www.commercialloandirect.com/dscr.html</a>
<br>
    <br>The Balance. (2024). A History of Commercial Mortgage-Backed Securities. <a href="https://www.thebalancemoney.com/introduction-to-cmbs-2866531">https://www.thebalancemoney.com/introduction-to-cmbs-2866531</a>
<br>
    <br>Bankrate. (2025). How Commercial Real Estate Loans Work. <a href="https://www.bankrate.com/loans/small-business/commercial-real-estate-loan/">https://www.bankrate.com/loans/small-business/commercial-real-estate-loan/</a>
<br>
    <br>J.P. Morgan Commercial Banking. (2025). Financing Your Commercial Property. <a href="https://www.jpmorgan.com/insights/real-estate/commercial-real-estate/commercial-real-estate-loans">https://www.jpmorgan.com/insights/real-estate/commercial-real-estate/commercial-real-estate-loans</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Registered Entity Ownership - The property is usually held in a Single Purpose Entity (SPE), typically an LLC, to isolate risk
<br>•   Loan-to-Value (LTV) Limits - Typically restricted to 65%-80% of the property's appraised value
<br>•   Minimum DSCR - Must demonstrate a Debt Service Coverage Ratio of 1.15x to 1.35x
<br>•   Environmental Compliance - Must pass a Phase I Environmental Site Assessment (ESA) to check for contamination
<br>•   Property Appraisal - A certified third-party appraisal commissioned by the lender is mandatory
<br>•   Personal Guarantee - Usually required ("Recourse Loan"), though "Non-Recourse" options exist for high-value institutional deals
<br>•   Clear Title - Title insurance and a clean title search are required to ensure no other liens exist
<br>•   Zoning & Land Use - Verification that the intended business use complies with local municipal zoning laws


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Purchase Agreement - The signed contract to buy the property
<br>•   Property Appraisal Report - Determining the current market value
<br>•   Rent Roll - (For multi-tenant properties) A list of all tenants, lease terms, and monthly rents
<br>•   Income & Expense Statement - For the property specifically, covering the last 2-3 years
<br>•   Phase I Environmental Report - Assessment of potential soil or water contamination
<br>•   Personal Financial Statement (PFS) - Required for all major owners/guarantors
<br>•   Business Tax Returns - Last 3 years of federal and state filings
<br>•   Photographs & Site Plans - Visual evidence of the property's condition and layout
<br>•   Entity Documents - Articles of Organization and Operating Agreement for the LLC holding the property

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def commercialbankingrealestatefaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Commercial Banking<br>
    Real Estate Loan</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is a Commercial Banking Real Estate Loan?</u></b><br>
    •Answer: It is a loan provided by commercial banks to finance the purchase, construction, or refinancing of income-generating or business-use real estate such as offices, warehouses, or retail properties.
</p>

    <p><u><b>2. Who is eligible for a Commercial Real Estate Loan?</u></b><br>
    •Answer: Businesses, investors, or property owners with stable cash flows, acceptable credit history, and sufficient collateral are typically eligible.
</p>

    <p><u><b>3. What types of properties can be financed under this loan?</u></b><br>
    •Answer: Commercial offices, industrial buildings, retail spaces, hotels, mixed-use properties, and sometimes multi-family apartments used for investment purposes.
</p>

    <p><u><b>4. How is a Commercial Real Estate Loan repaid?</u></b><br>
    •Answer: Repayment is usually made through monthly installments consisting of principal and interest over a fixed or variable loan term.
</p>

    <p><u><b>5. What is the typical loan tenure?</u></b><br>
    •Answer: The tenure generally ranges from 5 to 25 years, depending on the property type, bank policy, and borrower risk profile.
</p>

    <p><u><b>6. How do banks determine the loan amount?</u></b><br>
    •Answer: Banks assess the property value, loan-to-value (LTV) ratio, borrower's financial strength, and projected cash flows from the property.
</p>

    <p><u><b>7. What is the Loan-to-Value (LTV) ratio in commercial real estate loans?</u></b><br>
    •Answer: LTV commonly ranges from 60% to 80%, meaning the borrower must contribute the remaining portion as equity.
</p>

    <p><u><b>8. What interest rates apply to Commercial Real Estate Loans?</u></b><br>
    •Answer: Interest rates may be fixed or floating and are generally higher than residential mortgage rates due to higher risk.
</p>

    <p><u><b>9. What collateral is required for this loan?</u></b><br>
    •Answer: The financed property itself is the primary collateral, and banks may also require additional guarantees or security.
</p>

    <p><u><b>10. Are there any prepayment penalties?</u></b><br>
    •Answer: Yes, many commercial real estate loans include prepayment penalties to compensate banks for early repayment.
</p>

    <p><u><b>11. How is risk assessed by banks in such loans?</u></b><br>
    •Answer: Banks evaluate market conditions, property income potential, borrower creditworthiness, and debt service coverage ratio (DSCR).
</p>

    <p><u><b>12. What is the Debt Service Coverage Ratio (DSCR)?</u></b><br>
    •Answer: DSCR measures the property's ability to generate enough income to cover debt obligations, usually expected to be above 1.2.
</p>

    <p><u><b>13. Can these loans be used for refinancing existing properties?</u></b><br>
    •Answer: Yes, commercial real estate loans are often used to refinance existing debt to improve cash flow or obtain better terms.
</p>

    <p><u><b>14. What are the advantages of Commercial Real Estate Loans?</u></b><br>
    •Answer: They enable large-scale property investment, long repayment periods, and potential tax benefits related to interest expenses.
</p>

    <p><u><b>15. What are the limitations of Commercial Real Estate Loans?</u></b><br>
    •Answer: High capital requirements, strict documentation, exposure to market risks, and potential interest rate fluctuations are key limitations.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def commercialbankingrealestatetwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Commercial Banking</b></u><br>
    Capital Type: Real Estate Loan</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Commercial real estate loans are appropriate for established and growth-stage businesses seeking to purchase, develop, or refinance property used for business operations or income generation.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Eligible entities include C-Corps, LLCs, S-Corps, partnerships, and sole proprietorships. Single-purpose entities are commonly used for property ownership.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Borrowers must demonstrate strong financials, credit history, and sufficient equity contribution. Existing debt levels are closely evaluated.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
These loans operate within the commercial debt and real estate finance market. Prior equity financing is acceptable, but lenders focus heavily on asset value and cash flow coverage.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Loan amounts typically range from $250,000 to tens of millions, depending on property value, loan-to-value ratios, and borrower strength.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
This financing does not correspond to equity rounds and is typically used during expansion, stabilization, or long-term asset acquisition phases.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds are usually disbursed in a single tranche at closing, though construction or development loans may follow a draw-based schedule.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Funds may be used for:
<br>•   Property acquisition
<br>•   Construction or renovation
<br>•   Refinancing existing real estate debt
<br>•   Owner-occupied or income-generating property
Use is strictly limited to real estate-related purposes.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk is moderate to high, influenced by property market conditions, interest rate changes, and long-term repayment obligations. The property serves as collateral.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
Costs include interest rates, closing costs, appraisal fees, and long loan terms. While no equity dilution occurs, long-term debt commitment is significant.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are moderate to high, including appraisals, environmental reports, legal fees, and lender origination fees.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
The approval and closing process typically takes 45-90 days, depending on due diligence, property complexity, and lender requirements.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
