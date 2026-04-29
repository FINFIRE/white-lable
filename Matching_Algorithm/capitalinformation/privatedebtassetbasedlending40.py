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
def privatedebtassetbasedlending(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Debt</b></u><br>
    Capital Type: Asset Based Lending </center></p>
    <p><b><u>Introduction</u></b><br>
Asset-Based Lending (ABL) within the private debt market is ideal for companies seeking a flexible, revolving credit line or term loan secured by specific liquid assets like accounts receivable, inventory, and equipment. It is designed so that capital-intensive businesses—particularly those in transition, rapid growth, or with seasonal cycles—can maximize liquidity based on the value of their "collateral" rather than just their "cash flow." {n} fits that definition. Private ABL has surged in popularity as traditional banks have moved toward more conservative, cash-flow-only underwriting. In 2026, private debt funds and non-bank lenders (like Ares Management or White Oak) have filled the gap, offering more aggressive "advance rates" than banks. While a bank might lend 80% against receivables, a private ABL lender might go as high as 90%. Facilities typically range from $1 million to over $100 million, with interest rates usually priced at a spread over SOFR (Secured Overnight Financing Rate), often totaling 9% to 13% in the current market. While private ABL provides significantly more liquidity and fewer financial covenants than a bank, the trade-offs include higher interest rates, more frequent reporting requirements, and the risk of a "liquidity block" if the quality of your collateral declines.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.Private Asset-Based Lending is a secured structured finance product where the loan amount is determined by a "Borrowing Base." This base is a live calculation: for example, (85% of Eligible A/R) + (50% of Finished Goods Inventory) - (Priority Payables). Unlike traditional debt, the limit fluctuates daily or weekly as your business generates more invoices or builds more stock. (Investopedia, 2026)
<br>



    <br>2.  The best type of companies to raise private ABL are manufacturers, distributors, and wholesalers with high asset turnover. It is also a "rescue" tool for companies with high revenue but temporary losses, as private lenders care more about the "liquidation value" of the assets than the current P&L. If you can prove your customers pay their bills on time, you can secure an ABL line. (Secured Finance Network, 2025)
<br>

    <br>3. Private ABL emerged as a dominant force following the 2008 and 2023 banking crises. As commercial banks faced stricter "Capital Adequacy" rules, they were forced to exit riskier or more complex asset-heavy deals. This birthed the "Non-Bank ABL" market. In 2026, many private ABL lenders utilize AI-driven audit tools that integrate directly with a borrower's accounting software to provide instant daily funding. (ABF Journal, 2025)
<br>

    <br>4.While ABL offers a "flexible ceiling," it carries "monitoring and audit" risks. Lenders will perform "Field Exams" (site visits) multiple times a year. If your inventory is found to be "slow-moving" or obsolete, the lender can instantly remove it from your borrowing base, creating a "Liquidity Crunch" where you might suddenly owe the lender more than the base allows (an "Over-advance"). (White Oak Global, 2026)
<br>

    <br>5.
To raise capital via private ABL, a business must demonstrate "Collateral Quality." The lender will conduct a "Quality of Assets" (QoA) audit instead of a traditional bank "Quality of Earnings" (QoE) audit. You must be prepared to move your collections into a "Blocked Account" or "Lockbox" controlled by the lender, which ensures the lender is paid first before any excess cash is released back to the business for operations. (J.P. Morgan, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Investopedia.. Investopedia. (2026, Jan 05). Asset-Based Lending: Meaning, Types, and Borrowing Base.. <a href="https://www.investopedia.com/terms/a/assetbasedlending.asp">https://www.investopedia.com/terms/a/assetbasedlending.asp</a>
<br>

    <br>Secured Finance Network (SFNet). (2025). The State of the Asset-Based Lending Industry. <a href="https://www.sfnet.com/home/industry-data-publications">https://www.sfnet.com/home/industry-data-publications</a>
<br>

    <br>ABF Journal.. ABF Journal. (2025, Sept 12). Trends in Non-Bank ABL and Private Credit.. <a href="https://www.abfjournal.com/">https://www.abfjournal.com/</a>
<br>

    <br>White Oak Global. (2026). A Guide to Asset-Based Lending for Mid-Market Businesses. <a href="https://whiteoaksf.com/asset-based-lending/">https://whiteoaksf.com/asset-based-lending/</a>
<br>

    <br>J.P. Morgan Commercial Banking. (2025). How Asset-Based Lending Provides Liquidity. <a href="https://www.jpmorgan.com/insights/banking/commercial-loans/asset-based-lending">https://www.jpmorgan.com/insights/banking/commercial-loans/asset-based-lending</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   UCC-1 Priority – The lender must be able to file a public lien (Uniform Commercial Code) and hold the "First Priority" position on all pledged assets.
<br>•   Eligible Accounts Receivable – Invoices must generally be under 90 days old and not from "related parties" or foreign entities (unless insured).
<br>•   Inventory Verification – The business must have a perpetual inventory system that can be audited at any time.
<br>•   No Tax Liens – The business must be current on payroll and sales taxes, as tax liens usually take "super-priority" over a lender's claim.
<br>•   Lockbox Agreement – Legal requirement to redirect customer payments to a lender-controlled bank account.
<br>•   Cross-Collateralization – Often required, meaning all company assets (not just the ones on the borrowing base) secure the entire debt.
<br>•   Reporting Covenants – Legal obligation to provide a "Borrowing Base Certificate" (BBC) on a weekly or monthly basis.


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   A/R Aging Report – Detailed breakdown of who owes you money and for how long.
<br>•   Inventory Summary – List of Raw Materials, Work-in-Progress (WIP), and Finished Goods.
<br>•   Borrowing Base Certificate (Sample) – The calculation showing how much you expect to borrow.
<br>•   Accounts Payable (A/P) Aging – To ensure you aren't hiding debt that could result in liens.
<br>•   UCC Search Report – Verification that no other lenders have a claim on your assets.
<br>•   Financial Statements (Last 2 Years) – To prove operational stability.
<br>•   Customer Concentration Report – Showing that you aren't over-reliant on a single buyer.
<br>•   Articles of Incorporation – Proof of legal entity and ownership.

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def privatedebtassetbasedlendingfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Debt<br>
    Asset Based Lending</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is asset-based lending (ABL)?</u></b><br>
    •Answer: Asset-based lending is a form of private debt financing where a loan is secured by a company's assets, such as accounts receivable, inventory, equipment, or real estate.
</p>

    <p><u><b>2. Which assets are commonly used as collateral in ABL?</u></b><br>
    •Answer: Common collateral includes accounts receivable, inventory, machinery and equipment, and sometimes real estate or intellectual property.
</p>

    <p><u><b>3. Who typically uses asset-based lending?</u></b><br>
    •Answer: ABL is commonly used by small to mid-sized businesses, companies with strong assets but weaker cash flow, and firms undergoing growth, restructuring, or turnaround situations.
</p>

    <p><u><b>4. How is borrowing capacity determined in ABL?</u></b><br>
    •Answer: Borrowing capacity is based on a percentage of the value of eligible assets, often referred to as the borrowing base.
</p>

    <p><u><b>5. Is asset-based lending different from traditional bank loans?</u></b><br>
    •Answer: Yes, traditional loans rely more on cash flow and creditworthiness, while ABL focuses primarily on the value and quality of collateral.
</p>

    <p><u><b>6. What are the advantages of asset-based lending?</u></b><br>
    •Answer: Advantages include higher borrowing availability, flexibility, access to capital despite lower credit ratings, and scalability as asset values grow.
</p>

    <p><u><b>7. What are the risks of asset-based lending?</u></b><br>
    •Answer: Risks include asset seizure upon default, frequent monitoring requirements, and potential liquidity issues if asset values decline.
</p>

    <p><u><b>8. How quickly can asset-based loans be funded?</u></b><br>
    •Answer: Funding can occur relatively quickly, often within weeks, depending on asset appraisal, due diligence, and legal documentation.
</p>

    <p><u><b>9. Do lenders monitor assets after the loan is issued?</u></b><br>
    •Answer: Yes, lenders regularly monitor collateral through audits, reporting requirements, and asset revaluations.
</p>

    <p><u><b>10. Can startups qualify for asset-based lending?</u></b><br>
    •Answer: Startups may qualify if they have sufficient tangible assets, though ABL is more common among established or asset-heavy businesses.
</p>

    <p><u><b>11. What interest rates apply to asset-based loans?</u></b><br>
    •Answer: Interest rates are typically higher than traditional bank loans but lower than unsecured private debt, reflecting reduced risk due to collateral.
</p>

    <p><u><b>12. Can asset-based lending be used alongside other financing?</u></b><br>
    •Answer: Yes, ABL is often combined with equity financing, mezzanine debt, or revolving credit facilities.
</p>

    <p><u><b>13. What industries commonly use asset-based lending?</u></b><br>
    •Answer: Common industries include manufacturing, retail, distribution, transportation, and wholesale businesses.
</p>

    <p><u><b>14. Is asset-based lending suitable for distressed companies?</u></b><br>
    •Answer: Yes, ABL is frequently used in turnaround or distressed situations where asset values remain strong despite operational challenges.
</p>

    <p><u><b>15. How can a company qualify for asset-based lending?</u></b><br>
    •Answer: Companies can qualify by maintaining high-quality assets, accurate financial reporting, strong asset controls, and transparent operational practices.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def privatedebtassetbasedlendingtwelve(request):
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
    Capital Type: Asset Based Lending</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Asset Based Lending is best suited for operating businesses with established assets and ongoing cash flow. It is commonly used by growth-stage to mature companies, rather than early-stage startups.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
ABL is available to LLCs, S-Corps, and C-Corps. Sole proprietorships may qualify in limited cases, but lenders generally prefer formal business entities with audited or reviewed financials.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Businesses must demonstrate qualifying assets, such as accounts receivable, inventory, equipment, or other tangible assets. ABL lenders focus more on asset quality and liquidity than on profitability.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
ABL operates in the private credit market, with capital provided by non-bank lenders, private credit funds, and specialty finance companies.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Capital availability is tied to borrowing base formulas, typically:
· 70–90% of eligible accounts receivable
· 40–60% of inventory
· Lower advance rates for equipment
Total facilities commonly range from $500,000 to tens of millions of dollars.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Asset Based Lending is non-equity and non-round-based. It is often used alongside equity rounds or as an alternative to traditional bank debt.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds are usually provided through a revolving credit facility, allowing borrowers to draw and repay capital based on asset levels and working capital needs.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Permitted uses include:
<br>•   Working capital
<br>•   Inventory purchases
<br>•   Payroll and operating expenses
<br>•   Growth financing
Restrictions generally prohibit dividends, speculative investments, or unrelated business activities.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk is moderate, with lender risk mitigated by collateral. Borrowers face risks related to tight covenants, frequent reporting requirements, and asset revaluations.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
Cost of capital is higher than traditional bank loans but lower than unsecured private debt. Costs include interest rates, monitoring fees, and collateral management expenses.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are moderate to high, including due diligence fees, legal costs, appraisal fees, and field examination expenses.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital is relatively fast, typically 30–60 days, depending on asset verification, documentation, and lender underwriting.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
