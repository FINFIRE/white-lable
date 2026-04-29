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

def commercialbankingcollateralizeddebt(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Commercial Banking</b></u><br>
    Capital Type: Collateralized Debt </center></p>
    <p><b><u>Introduction</u></b><br>
Collateralized Debt is ideal for established companies seeking to leverage their existing assets—such as real estate, equipment, or high-value inventory—to secure lower interest rates and higher loan amounts. It is designed so that the lender's risk is mitigated by a physical or financial "backstop," allowing privately held businesses to access significant capital even if their cash flow is seasonal or currently being reinvested in growth. {n} fits that definition. Collateralized lending is the oldest and most stable segment of the commercial banking world. In 2026, as interest rates remain a primary concern for CFOs, collateralized debt continues to offer a "risk premium" discount; typically, a secured loan carries an interest rate 2% to 4% lower than an equivalent unsecured line of credit. On average, businesses can borrow against 70% to 80% of their asset's appraised value (Loan-to-Value). While collateralized debt provides cheaper and more abundant capital, the primary risk is the potential for asset seizure. If the business fails to meet its obligations, the bank has the legal right to foreclose on or repossess the pledged collateral to satisfy the debt.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.Collateralized Debt is a loan or credit facility where the borrower pledges specific assets as a security interest. In the event of a default, the lender becomes a "secured creditor," giving them a priority legal claim to sell those assets to recover the principal. Common collateral includes "Hard Assets" (Real Estate, Machinery) and "Soft Assets" (Accounts Receivable, Securities). (Investopedia, 2026)
<br>


    <br>2.  The best type of companies to raise capital via collateralized debt are capital-intensive firms with a high "Tangible Net Worth." This includes trucking companies (using their fleet), medical practices (using specialized equipment), and real estate firms. It is also an excellent tool for companies with a temporary "earnings dip" who still possess strong balance sheets, as the bank focuses on the value of the asset rather than just the last 12 months of profit. (Forbes Advisor, 2025)
<br>

    <br>3. Collateralized lending emerged in the early 20th century as banks sought more formal protections than simple "handshake" loans. The 1952 adoption of the Uniform Commercial Code (UCC) revolutionized the market by creating a standardized legal framework for "Perfecting a Security Interest." In 2026, the market has expanded into "Cross-Collateralization," where multiple assets are bundled together to secure a larger, more flexible credit facility. (UCC Law Journal, 2025)
<br>
    <br>4.While secured debt is cheaper, it carries "liquidity and operational" risks. Pledging an asset often involves a "Negative Pledge" covenant, which legally prevents the business from using that same asset to secure any other loans. Additionally, if the market value of the collateral drops significantly, the bank may issue a "Margin Call," requiring the borrower to pay down a portion of the loan immediately to maintain the required Loan-to-Value (LTV) ratio. (Corporate Finance Institute, 2025)
<br>
    <br>5.
To raise capital via collateralized debt, a company must provide an independent appraisal of the assets. The lender will perform a "Lien Search" to ensure the assets are "Free and Clear" of other encumbrances. Once approved, the lender "perfects" their interest by filing a UCC-1 Financing Statement with the Secretary of State, which acts as a public notice that the bank has a legal claim to the property. (J.P. Morgan, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Investopedia. (2026). Collateralized Debt: Meaning, Types, and Risks. <a href="https://www.investopedia.com/terms/c/collateralizeddebt.asp">https://www.investopedia.com/terms/c/collateralizeddebt.asp</a>
<br>
    <br>Forbes Advisor. (2025). Secured vs. Unsecured Business Loans: Which is Right for You? <a href="https://www.forbes.com/advisor/business-loans/secured-vs-unsecured-business-loans/">https://www.forbes.com/advisor/business-loans/secured-vs-unsecured-business-loans/</a>
<br>
    <br>Corporate Finance Institute (CFI). (2025). Understanding Security Interests and Collateral. <a href="https://corporatefinanceinstitute.com/resources/commercial-lending/collateral/">https://corporatefinanceinstitute.com/resources/commercial-lending/collateral/</a>
<br>
    <br>UCC Law Journal. (2025). Developments in Perfection and Priority of Security Interests. <a href="https://www.americanbar.org/groups/business_law/publications/the_business_lawyer/">https://www.americanbar.org/groups/business_law/publications/the_business_lawyer/</a>
<br>
    <br>J.P. Morgan Commercial Banking. (2025). Asset-Based vs. Cash Flow Lending. <a href="https://www.jpmorgan.com/insights/banking/business-loans/asset-based-lending">https://www.jpmorgan.com/insights/banking/business-loans/asset-based-lending</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Evidence of Ownership - Must provide clear title, deeds, or bills of sale for the pledged assets
<br>•   Lien Priority - The lender typically requires a "First Priority" position (no existing liens from other banks)
<br>•   Loan-to-Value (LTV) Limits - Generally capped at 70-80% for real estate and 50-70% for equipment/inventory
<br>•   Insurance Coverage - Mandatory "Loss Payee" clause on business insurance, naming the bank as a beneficiary
<br>•   UCC-1 Filing - Public registration of the security interest with the state
<br>•   Maintenance Covenants - Legal requirement to keep the collateral in good working order
<br>•   Appraisal Validity - Appraisals must be performed by a certified, lender-approved third party


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Asset Appraisal Report - Determining the current fair market value (FMV)
<br>•   UCC Search Results - Verification that no other liens exist on the property
<br>•   Title Insurance - For loans involving commercial real estate
<br>•   Equipment List with Serial Numbers - Detailed inventory of assets being pledged
<br>•   Insurance Certificate - Proof of coverage with the lender listed as "Additional Insured"
<br>•   Business Financial Statements - Last 2-3 years (to prove the ability to pay the interest)
<br>•   Corporate Resolution - Authorization from the board/owners to pledge company assets

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def commercialbankingcollateralizeddebtfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Commercial Banking<br>
    Collateralized Debt</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is collateralized debt in commercial banking?</u></b><br>
    •Answer: Collateralized debt is a form of commercial bank financing where a loan is secured by specific business or personal assets, giving the lender the right to seize the collateral if the borrower defaults.
</p>

    <p><u><b>2. What types of collateral are commonly used for collateralized debt?</u></b><br>
    •Answer: Common collateral includes real estate, equipment, inventory, accounts receivable, vehicles, and in some cases personal assets or cash deposits.
</p>

    <p><u><b>3. What types of businesses are best suited for collateralized debt?</u></b><br>
    •Answer: Businesses with valuable, easily appraisable assets and stable operations are best suited for collateralized debt financing.
</p>

    <p><u><b>4. How much funding can be obtained through collateralized debt?</u></b><br>
    •Answer: Loan amounts typically depend on the value of the collateral, with lenders offering 50%-80% of the appraised asset value.
</p>

    <p><u><b>5. How quickly can funds be accessed with collateralized debt?</u></b><br>
    •Answer: Funding timelines generally range from a few weeks to several months, depending on asset valuation, documentation, and credit approval processes.
</p>

    <p><u><b>6. How do interest rates compare to unsecured loans?</u></b><br>
    •Answer: Interest rates on collateralized debt are usually lower than unsecured loans because the lender's risk is reduced by the pledged assets.
</p>

    <p><u><b>7. Is personal guarantee required for collateralized debt?</u></b><br>
    •Answer: In many cases, banks still require personal guarantees from business owners, especially for small or closely held businesses.
</p>

    <p><u><b>8. Can collateralized debt be used for any business purpose?</u></b><br>
    •Answer: Yes, collateralized debt can be used for working capital, equipment purchases, expansion, refinancing, or real estate acquisition, subject to lender approval.
</p>

    <p><u><b>9. What are the main advantages of collateralized debt?</u></b><br>
    •Answer: Advantages include lower interest rates, higher borrowing limits, longer repayment terms, and improved approval chances compared to unsecured debt.
</p>

    <p><u><b>10. What are the risks of using collateralized debt?</u></b><br>
    •Answer: Risks include loss of pledged assets in case of default, reduced flexibility in using collateral, and potential impact on future borrowing capacity.
</p>

    <p><u><b>11. Can collateralized debt be combined with other financing options?</u></b><br>
    •Answer: Yes, it is commonly combined with lines of credit, SBA loans, asset-based lending, or equity financing.
</p>

    <p><u><b>12. How does collateralized debt differ from asset-based lending?</u></b><br>
    •Answer: Collateralized debt uses specific pledged assets for security, while asset-based lending relies on a revolving borrowing base tied to ongoing asset values.
</p>

    <p><u><b>13. Is collateralized debt suitable for startups?</u></b><br>
    •Answer: Startups may qualify if owners can pledge personal assets, but lenders generally prefer established businesses with operating history.
</p>

    <p><u><b>14. What documentation is required for collateralized debt?</u></b><br>
    •Answer: Required documents include asset appraisals, financial statements, tax returns, legal agreements, and collateral security filings.
</p>

    <p><u><b>15. How can a business improve approval chances for collateralized debt?</u></b><br>
    •Answer: Approval chances improve by offering high-quality collateral, maintaining strong credit profiles, demonstrating repayment ability, and providing clear use-of-funds documentation.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def commercialbankingcollateralizeddebttwelve(request):
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
    Capital Type: Collateralized Debt</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Collateralized debt is best suited for operating, growth-stage, and mature businesses with stable cash flows and tangible assets. Startups may qualify only if strong collateral or guarantees are available.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Eligible entities include LLCs, corporations, partnerships, and established sole proprietorships. Banks require the borrower to be a legally registered business capable of pledging assets.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Borrowers must demonstrate creditworthiness, repayment capacity, and asset ownership. Banks typically review financial statements, credit history, tax returns, and collateral valuation before approval.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Collateralized debt operates within the formal commercial banking market, regulated by banking authorities and subject to underwriting standards and compliance requirements.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Loan amounts depend on the value of pledged collateral, often capped by a loan-to-value (LTV) ratio ranging from 60% to 80%. Funding can range from tens of thousands to millions of dollars.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
This financing is non-dilutive debt and does not represent an equity round. It is commonly used during expansion, asset acquisition, or refinancing phases of a business lifecycle.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds are usually disbursed in a single lump sum, though revolving or staged disbursement structures may be used depending on loan purpose and bank policy.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Permitted uses include equipment purchases, real estate acquisition, working capital, inventory financing, and refinancing existing debt. Use of funds is strictly monitored by the lender.
<br>•   Equipment purchases and real estate acquisition
<br>•   Working capital and inventory financing
<br>•   Refinancing existing debt
<br>•   Business expansion

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk to the lender is moderate, as collateral reduces exposure. Risk to the borrower is high, because default can result in asset seizure, foreclosure, or liquidation.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
Interest rates are generally lower than unsecured loans due to reduced lender risk. Rates vary based on credit profile, collateral quality, and market conditions.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs may include origination fees, appraisal fees, legal costs, and lien filing charges, making initial expenses higher than unsecured debt.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing is moderate, typically 4-12 weeks, due to collateral appraisal, underwriting, and regulatory approval processes.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
