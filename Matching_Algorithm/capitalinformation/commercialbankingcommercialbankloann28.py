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

def commercialbankingcommercialbankloann(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Commercial Banking</b></u><br>
    Capital Type: Commercial Bank Loan </center></p>
    <p><b><u>Introduction</u></b><br>
A Commercial Bank Loan is ideal for established companies seeking debt-based financing to fund major capital expenditures, cover operational costs, or manage seasonal working capital needs. It is designed so that regulated financial institutions can provide capital to registered business entities in exchange for regular interest payments and, typically, a claim on business assets as collateral. {n} fits that definition. Commercial lending is the backbone of the global economy, representing a massive share of total business funding. In 2024, data from the Federal Reserve and international banking reports indicated that commercial and industrial loans remained a primary driver for middle-market growth. Unlike venture capital, bank loans allow founders to retain 100% ownership. While terms vary, interest rates for prime borrowers in 2025 typically range from 7% to 9%, significantly lower than the 30%+ often seen with online alternative lenders. While bank loans offer the lowest cost of capital, their stringent eligibility requirements—including "time in business" (usually 2+ years) and the necessity of high-quality collateral—often make them inaccessible for early-stage startups or businesses with inconsistent cash flow.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.A Commercial Bank Loan is a financial agreement where a bank provides a lump sum (Term Loan) or an available credit limit (Line of Credit) to a business. These loans are strictly for business purposes—such as inventory procurement, payroll, or equipment acquisition—and are legally separate from personal credit. Lenders evaluate the "Five Cs of Credit": Character, Capacity, Capital, Collateral, and Conditions. (Investopedia, 2025)
<br>


    <br>2.  The best type of companies for these loans are "stable" enterprises with at least two years of profitable operation and a clear ability to service debt. Because banks are risk-averse, they prefer companies with tangible assets (real estate, machinery, or accounts receivable) that can be pledged as security. It is highly effective for manufacturers, retailers, and service providers with predictable, recurring revenue streams. (Bankrate, 2025)
<br>

    <br>3. Commercial lending evolved from early merchant banking into the highly regulated sector it is today. Historically, loans were primarily short-term "working capital" advances. Today, the market has diversified into specialized products like Commercial Mortgages and Equipment Financing. Since the 2008 and 2023 banking crises, regulations like Basel III have led banks to maintain stricter underwriting standards, making "stress-tested" financial statements a necessity for approval. (OCC.gov, 2025)
<br>
    <br>4.While bank loans provide stability, they carry the risk of "asset seizure." Most commercial loans are "secured," meaning the bank can confiscate property, plant, or equipment if the borrower defaults. Furthermore, banks often require restrictive covenants—legal agreements that require the business to maintain certain financial ratios (like a minimum Debt Service Coverage Ratio). Violating these covenants can trigger a "technical default," allowing the bank to call the loan due immediately. (Bajaj Finserv, 2025)
<br>
    <br>5.
To raise capital via a bank loan, a business must go through a formal underwriting process. This involves a deep dive by credit analysts into the company's historical performance and future projections. For many small-to-mid-sized businesses, the bank will also require a personal guarantee from the owners, meaning the owner's personal assets could be at risk if the business cannot repay the debt. (National Bank of Commerce, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Investopedia. (2025). Commercial Loan: What It Is, How It Works. <a href="https://www.investopedia.com/terms/c/commercial-loan.asp">https://www.investopedia.com/terms/c/commercial-loan.asp</a>
<br>
    <br>Bankrate. (2025). Pros and Cons of a Business Bank Loan. <a href="https://www.bankrate.com/loans/small-business/business-loan-pros-cons/">https://www.bankrate.com/loans/small-business/business-loan-pros-cons/</a>
<br>
    <br>OCC.gov. (2025). Comptroller's Handbook: Commercial Loans. <a href="https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/files/commercial-loans/pub-ch-commercial-loans.pdf">https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/files/commercial-loans/pub-ch-commercial-loans.pdf</a>
<br>
    <br>Bajaj Finserv. (2025). What is a Commercial Loan - Meaning & Definition. <a href="https://www.bajajfinserv.in/what-is-commercial-loan">https://www.bajajfinserv.in/what-is-commercial-loan</a>
<br>
    <br>National Bank of Commerce. (2025). How Business Loans Work: A Comprehensive Guide. <a href="https://www.nbcbanking.com/business-banking/business-lending-guide/how-business-loans-work/">https://www.nbcbanking.com/business-banking/business-lending-guide/how-business-loans-work/</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Business Registration - Must be a legally registered entity (LLC, C-Corp, Partnership) in good standing
<br>•   Time in Business - Typically a minimum of 24 months of active operations
<br>•   Profitability - Demonstrated "Debt Service Coverage Ratio" (DSCR) usually above 1.25x
<br>•   Credit Score - Strong business credit and personal credit for owners (often 680+)
<br>•   Collateral - Availability of tangible assets to secure the loan (LTV ratios typically capped at 70-80%)
<br>•   Legal Entity Identifier (LEI) - Increasingly required for larger commercial transactions
<br>•   Personal Guarantee - Usually required for any owner with a 20% or greater stake
<br>•   Insurance - Requirement to maintain business and/or key-man life insurance naming the bank as beneficiary


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Business Tax Returns - Full federal filings for the last 3 fiscal years
<br>•   Audited Financial Statements - Balance Sheets and Income Statements (P&L) for the last 3 years
<br>•   Interim Financials - P&L and Balance Sheet current within the last 45-90 days
<br>•   Accounts Receivable (A/R) Aging - A list of who owes the business money and for how long
<br>•   Articles of Incorporation - Legal formation and bylaws/operating agreements
<br>•   Personal Tax Returns - Last 3 years for all principal owners
<br>•   Business Plan & Projections - 1-3 year cash flow forecast with stated assumptions
<br>•   Debt Schedule - A list of all existing business liabilities, leases, and loans
<br>•   Appraisal Reports - Required for loans secured by real estate or heavy equipment

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def commercialbankingcommercialbankloannfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Commercial Banking<br>
    Commercial Bank Loan</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is a commercial bank loan?</u></b><br>
    •Answer: A commercial bank loan is a debt financing option provided by banks to businesses for operating needs, expansion, asset purchases, or refinancing, where the borrower repays the principal plus interest over a fixed or variable period.
</p>

    <p><u><b>2. What types of businesses are best suited for commercial bank loans?</u></b><br>
    •Answer: Established businesses with stable cash flows, good credit history, proven revenue, and the ability to provide collateral are best suited for commercial bank loans.
</p>

    <p><u><b>3. How much funding can a business receive through a commercial bank loan?</u></b><br>
    •Answer: Funding amounts vary widely and can range from $50,000 to several million dollars, depending on the business's financial strength, collateral, repayment capacity, and bank policies.
</p>

    <p><u><b>4. How quickly can a commercial bank loan be approved and funded?</u></b><br>
    •Answer: Approval and funding typically take 2 to 12 weeks, depending on documentation, credit evaluation, collateral appraisal, and internal bank approval processes.
</p>

    <p><u><b>5. What are the typical interest rates on commercial bank loans?</u></b><br>
    •Answer: Interest rates may be fixed or variable and are usually based on benchmarks such as the prime rate or SOFR, plus a margin determined by the borrower's risk profile.
</p>

    <p><u><b>6. What are the repayment terms for commercial bank loans?</u></b><br>
    •Answer: Repayment terms generally range from 1 to 10 years for working capital loans and up to 20-25 years for real estate-backed loans, with monthly or quarterly payments.
</p>

    <p><u><b>7. Is collateral required for a commercial bank loan?</u></b><br>
    •Answer: Yes, most commercial bank loans require collateral such as real estate, equipment, inventory, or personal guarantees from business owners to reduce lender risk.
</p>

    <p><u><b>8. Can startups qualify for commercial bank loans?</u></b><br>
    •Answer: Startups may find it difficult to qualify unless they have strong collateral, excellent personal credit, a solid business plan, or additional guarantees, as banks typically prefer established firms.
</p>

    <p><u><b>9. What documents are required to apply for a commercial bank loan?</u></b><br>
    •Answer: Required documents usually include financial statements, tax returns, cash flow projections, business plans, bank statements, and details of collateral and ownership structure.
</p>

    <p><u><b>10. Can commercial bank loans be used for any business purpose?</u></b><br>
    •Answer: Commercial bank loans can be used for various purposes such as working capital, equipment purchases, expansion, refinancing debt, or real estate acquisition, subject to bank approval.
</p>

    <p><u><b>11. What are the main advantages of commercial bank loans?</u></b><br>
    •Answer: Key advantages include lower interest rates compared to alternative financing, predictable repayment schedules, no equity dilution, and long-term funding stability.
</p>

    <p><u><b>12. What are the risks of using commercial bank loans?</u></b><br>
    •Answer: Risks include strict repayment obligations, collateral loss in case of default, restrictive loan covenants, and potential strain on cash flow during downturns.
</p>

    <p><u><b>13. How do commercial bank loans compare to SBA loans?</u></b><br>
    •Answer: Commercial bank loans often have stricter qualification criteria and higher collateral requirements, while SBA loans offer government guarantees that make approval easier for some businesses.
</p>

    <p><u><b>14. Can a business refinance a commercial bank loan?</u></b><br>
    •Answer: Yes, businesses can refinance commercial bank loans to obtain better interest rates, longer terms, or improved cash flow, subject to lender approval and market conditions.
</p>

    <p><u><b>15. How can a business improve its chances of getting approved for a commercial bank loan?</u></b><br>
    •Answer: Businesses can improve approval chances by maintaining strong financial statements, good credit scores, stable cash flow, clear loan purpose, and adequate collateral or guarantees.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def commercialbankingcommercialbankloanntwelve(request):
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
    Capital Type: Commercial Bank Loan</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Commercial bank loans are best suited for established businesses or late early-stage companies with operating history, predictable cash flows, and proven business models. Startups may qualify only with strong collateral, guarantees, or existing revenue.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Eligible entities include C-Corps, LLCs, S-Corps, partnerships, and sole proprietorships. Banks typically prefer formally registered entities with clear ownership structures and financial records.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Businesses are expected to demonstrate existing revenue, positive or improving cash flow, and creditworthiness. Prior capital raises are acceptable, but excessive leverage may reduce approval chances.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
This financing operates within the private debt market through regulated financial institutions. Previous equity or debt financing is reviewed to assess risk, repayment ability, and capital structure.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Commercial bank loans can range from small working-capital loans to multi-million-dollar facilities, depending on business size, collateral, financial performance, and credit profile.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
This financing does not align with traditional equity rounds. It is typically used during growth, expansion, or stabilization phases rather than pre-seed or seed stages.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds are usually disbursed in a single lump sum, though revolving facilities or term loans with staged disbursements may be structured based on project needs.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Loan proceeds may be used for:
<br>•   Working capital
<br>•   Equipment or asset purchases
<br>•   Business expansion
<br>•   Inventory or operational costs
Restrictions often prohibit use for personal expenses, speculative investments, or unrelated ventures.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk is moderate, as repayment obligations are fixed regardless of business performance. Failure to repay can lead to asset seizure, credit damage, or personal guarantee enforcement.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
Cost of capital includes interest payments, fees, and opportunity cost of collateral. Compared to equity, dilution is avoided, but financial pressure from repayment obligations is higher.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs may include application fees, legal fees, appraisal costs, and documentation charges, generally moderate depending on loan size and complexity.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
The approval and funding process typically takes 1-3 months, depending on underwriting, documentation, and collateral evaluation. Larger or more complex loans may take longer.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
