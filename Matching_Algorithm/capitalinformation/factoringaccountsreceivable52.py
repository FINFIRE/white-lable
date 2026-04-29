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

def factoringaccountsreceivable(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Factoring</b></u><br>
    Capital Type: Accounts Receivable Loans </center></p>
    <p><b><u>Introduction</u></b><br>
Accounts Receivable Loans are ideal for companies that generate consistent invoiced revenues but experience cash-flow gaps due to extended customer payment terms. They are designed so that capital is advanced against outstanding accounts receivable, allowing businesses to unlock working capital without issuing equity or taking on long-term debt. {n} fits that definition. In 2026, accounts receivable-based financing remains a critical liquidity tool for small, mid-market, and asset-light businesses across sectors such as manufacturing, logistics, staffing, wholesale, and B2B services. As payment cycles lengthen and supply chains remain volatile, factoring and receivables lending have gained renewed importance as alternatives to traditional bank lines of credit. While receivables loans improve cash flow predictability, they introduce counterparty, dilution, and operational risk. Funding availability depends on customer credit quality, invoice enforceability, and ongoing reporting accuracy. Poor customer payment performance or disputes can reduce borrowing capacity and increase financing costs.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.An Accounts Receivable Loan is a form of asset-based financing in which a lender advances funds to a business based on the value of its outstanding customer invoices, typically expressed as a percentage of eligible receivables. Ownership of the receivables generally remains with the borrower. (Corporate Finance Institute, 2026)
<br>


    <br>2.  Accounts receivable loans occupy a senior position within the Capital Stack, usually as senior secured debt backed by a first-priority lien on receivables and related proceeds. In the event of insolvency, lenders have priority claims over collections from pledged invoices. (Moody's Investors Service, 2025)
<br>

    <br>3. Legally, accounts receivable loans are governed by a Loan and Security Agreement that defines advance rates, eligibility criteria, borrowing base calculations, reporting obligations, and default remedies. Security is typically perfected through UCC filings over receivables and cash accounts. (Latham & Watkins, 2025)
<br>
    <br>4.From a risk perspective, receivable-based lending transfers dilution risk away from equity holders while introducing customer credit risk, concentration risk, and operational execution risk. Disputed, aged, or concentrated receivables can materially reduce borrowing availability. (S&P Global Ratings, 2025)
<br>
    <br>5.
From an accounting and process standpoint, accounts receivable loans are recorded as Short-Term Liabilities, with interest and fees recognized as financing expenses. Borrowers must provide frequent reporting—often weekly or monthly—making these facilities operationally intensive but highly responsive to revenue growth. (Deloitte, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Corporate Finance Institute (CFI). (2026). Accounts Receivable Financing and Factoring. <a href="https://corporatefinanceinstitute.com/resources/credit-analysis">https://corporatefinanceinstitute.com/resources/credit-analysis</a>
<br>
    <br>Moody's Investors Service. (2025). Asset-Based Lending and Receivables Risk. <a href="https://www.moodys.com/asset-based-lending">https://www.moodys.com/asset-based-lending</a>
<br>
    <br>Latham & Watkins. (2025). Receivables Financing: Legal Structures. <a href="https://www.lw.com/receivables-finance">https://www.lw.com/receivables-finance</a>
<br>
    <br>S&P Global Ratings. (2025). Working Capital Financing Risks. <a href="https://www.spglobal.com/ratings">https://www.spglobal.com/ratings</a>
<br>
    <br>Deloitte. (2025). Accounting for Asset-Based Lending. <a href="https://www2.deloitte.com/asset-based-lending">https://www2.deloitte.com/asset-based-lending</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Eligible Receivables - Invoices to creditworthy customers
<br>•   Advance Rate Limits - Typically 70%-90% of eligible AR
<br>•   Borrowing Base Reporting - Regular AR aging and reconciliations
<br>•   Security Interest - First-priority lien on receivables and proceeds
<br>•   Concentration Limits - Caps on exposure to single customers
<br>•   Dilution Thresholds - Returns, credits, and disputes monitoring
<br>•   Lockbox / Control Account - Lender-controlled cash collections
<br>•   Regulatory Compliance - Commercial lending and UCC requirements


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Loan & Security Agreement - Primary financing contract
<br>•   Borrowing Base Certificate - Receivables availability calculation
<br>•   Accounts Receivable Aging Report - Invoice detail
<br>•   UCC Filings - Perfection of security interest
<br>•   Lockbox Agreement - Cash control arrangement
<br>•   Customer Contracts & Invoices - Proof of receivables
<br>•   Financial Statements - Historical and projected
<br>•   Board Resolutions - Authorization to incur debt

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def factoringaccountsreceivablefaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Factoring<br>
    Accounts Receivable Loans</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is accounts receivable factoring?</u></b><br>
    •Answer: Accounts receivable factoring is a financing arrangement where a business sells its unpaid invoices to a factoring company in exchange for immediate cash.
</p>

    <p><u><b>2. Who provides accounts receivable factoring?</u></b><br>
    •Answer: Factoring is provided by specialized factoring companies, alternative lenders, and some non-bank financial institutions.
</p>

    <p><u><b>3. When is accounts receivable factoring typically used?</u></b><br>
    •Answer: It is commonly used to improve cash flow, manage working capital gaps, and fund operations while waiting for customers to pay invoices.
</p>

    <p><u><b>4. How does accounts receivable factoring work?</u></b><br>
    •Answer: The business sells invoices to the factor, receives an advance (usually a percentage of the invoice value), and the factor collects payment from the customer.
</p>

    <p><u><b>5. What percentage of invoice value is typically advanced?</u></b><br>
    •Answer: Factors typically advance 70% to 90% of the invoice value, depending on customer credit quality and invoice terms.
</p>

    <p><u><b>6. Is factoring a loan or a sale?</u></b><br>
    •Answer: Factoring is technically a sale of receivables, not a traditional loan, although it functions similarly to short-term financing.
</p>

    <p><u><b>7. What fees are charged in accounts receivable factoring?</u></b><br>
    •Answer: Fees usually include a factoring fee or discount rate, calculated as a percentage of the invoice value and based on payment timing and risk.
</p>

    <p><u><b>8. Is collateral required for factoring?</u></b><br>
    •Answer: The invoices themselves serve as collateral, so no additional assets are typically required.
</p>

    <p><u><b>9. Who bears the credit risk in factoring?</u></b><br>
    •Answer: In non-recourse factoring, the factor bears the customer's non-payment risk; in recourse factoring, the business retains the risk.
</p>

    <p><u><b>10. How quickly can funds be received through factoring?</u></b><br>
    •Answer: Funds can often be received within 24 to 72 hours after invoice verification.
</p>

    <p><u><b>11. Does factoring affect customer relationships?</u></b><br>
    •Answer: It can, as customers may pay the factor directly, but many factors manage collections professionally to minimize disruption.
</p>

    <p><u><b>12. What are the benefits of accounts receivable factoring?</u></b><br>
    •Answer: Benefits include improved cash flow, reduced collection burden, faster access to working capital, and financing based on customer credit.
</p>

    <p><u><b>13. What are the risks of factoring?</u></b><br>
    •Answer: Risks include higher costs than bank loans, potential customer perception issues, and dependence on invoice volume.
</p>

    <p><u><b>14. How does factoring differ from accounts receivable loans?</u></b><br>
    •Answer: In factoring, invoices are sold to the factor, while in accounts receivable loans, invoices are pledged as collateral for a loan.
</p>

    <p><u><b>15. When should a business consider accounts receivable factoring?</u></b><br>
    •Answer: A business should consider factoring when it has strong receivables, long payment cycles, and needs immediate working capital without taking on traditional debt.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def factoringaccountsreceivabletwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Factoring</b></u><br>
    Capital Type: Accounts Receivable Loans</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Accounts receivable factoring is best suited for revenue-generating companies that have begun issuing invoices to customers, typically from early revenue stage through growth and mature stages. The company's age is less critical than the presence of consistent invoicing and creditworthy customers, making factoring unsuitable for pre-revenue startups.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
C-Corporations and LLCs are the preferred entity types for accounts receivable factoring, as these structures support enforceable contracts, clear ownership of receivables, and standard accounting practices. Sole proprietorships may qualify in limited cases but are generally less attractive due to higher risk and weaker financial separation.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Factoring can be accessed regardless of prior equity or debt raises, as underwriting is primarily based on the quality of the accounts receivable rather than the company's capitalization. Companies with limited operating history or constrained balance sheets may still qualify if their customers demonstrate strong payment reliability.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Accounts receivable factoring operates within the private asset-based lending and alternative finance market. Providers include specialized factoring companies, private credit funds, fintech lenders, and non-bank financial institutions focused on working capital solutions.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
The amount of capital available through factoring is directly tied to the value of outstanding receivables and typically ranges from tens of thousands to several million dollars. Advance rates are commonly a percentage of invoice value, with total availability fluctuating as new receivables are generated.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Factoring is not considered a capital round and does not involve valuation or equity issuance. It is used as an ongoing working capital facility that converts receivables into immediate cash to support operations and growth.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds are disbursed on a rolling basis as invoices are issued and approved by the factoring provider. Each invoice effectively represents a separate tranche, with advances paid upfront and remaining balances released upon customer payment, net of fees.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Factoring proceeds are commonly used to cover:
<br>•   Payroll and operating expenses
<br>•   Inventory purchases and vendor payments
<br>•   General working capital needs
Use of funds is typically unrestricted, provided receivables remain valid and collectible.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk to the factoring provider is primarily tied to customer non-payment, while risk to the company includes fees, potential recourse obligations, and customer relationship considerations. Companies may also face concentration risk if a small number of customers account for most receivables.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital includes factoring fees, discount rates, and potential service charges, which are generally higher than traditional bank lines of credit but lower than unsecured short-term debt. Costs reflect the speed, flexibility, and credit risk assumed by the provider.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are moderate and may include setup fees, legal documentation, due diligence on receivables, and system integration for invoice verification. Costs can increase with complex customer structures or high-volume invoicing requirements.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital is relatively fast, often ranging from one to three weeks for initial setup. Once established, funding against approved invoices can occur within days, providing ongoing liquidity.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
