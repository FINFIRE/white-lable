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

def factoringinvoice(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Factoring</b></u><br>
    Capital Type: Invoice Factoring </center></p>
    <p><b><u>Introduction</u></b><br>
Invoice Factoring is ideal for businesses that generate invoiced sales but face delayed customer payments that constrain working capital. It is designed so that a company sells its outstanding invoices to a factoring provider at a discount in exchange for immediate cash, allowing operations to continue without issuing equity or taking on traditional debt. {n} fits that definition. In 2026, invoice factoring remains a widely used financing solution across industries such as manufacturing, logistics, staffing, wholesale, and professional services. As payment terms extend and supply chains grow more complex, factoring provides a flexible alternative to bank credit lines, particularly for small and mid-sized enterprises and fast-growing companies. While invoice factoring improves liquidity and cash-flow visibility, it introduces customer credit dependency, cost, and reputational risk. Funding availability and pricing depend heavily on the credit quality of end customers, and poor communication or disputes can disrupt collections and financing continuity.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.Invoice Factoring is a form of receivables financing in which a business sells its outstanding invoices to a third-party factor at a discount, receiving immediate cash while the factor assumes responsibility for collecting payment from customers. (Investopedia, 2025)
<br>


    <br>2.  Invoice factoring sits outside the traditional Capital Stack, as it is structured as a sale of receivables rather than a loan or equity investment. The factor does not obtain ownership in the business, but instead acquires rights to the specified invoices. (Corporate Finance Institute, 2026)
<br>

    <br>3. Legally, invoice factoring is governed by a Factoring Agreement that defines advance rates, discount fees, recourse or non-recourse terms, collection authority, and dispute resolution mechanisms. Ownership of the receivables is transferred to the factor upon sale. (Latham & Watkins, 2025)
<br>
    <br>4.From a risk perspective, invoice factoring transfers customer payment and collection risk to the factor in non-recourse structures, while recourse arrangements leave ultimate credit risk with the seller. Businesses also face concentration and reputational risk tied to customer interactions. (S&P Global Ratings, 2025)
<br>
    <br>5.
From an accounting and process standpoint, invoice factoring is typically recorded as a Sale of Receivables rather than debt, provided control and risk transfer criteria are met. Funding can be accessed quickly, but costs are generally higher than traditional secured lending. (Deloitte, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Investopedia. (2025). Invoice Factoring Definition. <a href="https://www.investopedia.com/invoice-factoring">https://www.investopedia.com/invoice-factoring</a>
<br>
    <br>Corporate Finance Institute (CFI). (2026). Factoring vs. Accounts Receivable Financing. <a href="https://corporatefinanceinstitute.com/resources/credit-analysis">https://corporatefinanceinstitute.com/resources/credit-analysis</a>
<br>
    <br>Latham & Watkins. (2025). Receivables Sales and Factoring Agreements. <a href="https://www.lw.com/receivables-finance">https://www.lw.com/receivables-finance</a>
<br>
    <br>S&P Global Ratings. (2025). Credit Risk in Receivables-Based Finance. <a href="https://www.spglobal.com/ratings">https://www.spglobal.com/ratings</a>
<br>
    <br>Deloitte. (2025). Accounting for Sales of Receivables. <a href="https://www2.deloitte.com/receivables-accounting">https://www2.deloitte.com/receivables-accounting</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Eligible Invoices - Valid, undisputed customer invoices
<br>•   Creditworthy Customers - Approved debtor credit profiles
<br>•   Recourse vs. Non-Recourse Structure - Risk allocation terms
<br>•   Assignment of Receivables - Legal transfer of invoice ownership
<br>•   Notification Requirements - Customer payment instructions
<br>•   Concentration Limits - Exposure caps by customer
<br>•   Dilution Controls - Returns, credits, and offsets monitoring
<br>•   Regulatory Compliance - Commercial finance and disclosure laws


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Factoring Agreement - Primary receivables sale contract
<br>•   Schedule of Invoices - Invoices sold to the factor
<br>•   Customer Contracts - Proof of payment obligations
<br>•   Notice of Assignment - Customer payment redirection
<br>•   Accounts Receivable Aging - Invoice status reporting
<br>•   Bank & Lockbox Agreements - Collection controls
<br>•   Financial Statements - Seller financial condition
<br>•   Board Resolutions - Authorization to enter factoring arrangement

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def factoringinvoicefaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Factoring<br>
    Invoice Factoring</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is invoice factoring?</u></b><br>
    •Answer: Invoice factoring is a financing method where a business sells its unpaid invoices to a factoring company in exchange for immediate cash.
</p>

    <p><u><b>2. Who provides invoice factoring?</u></b><br>
    •Answer: Invoice factoring is provided by specialized factoring companies, alternative lenders, and some non-bank financial institutions.
</p>

    <p><u><b>3. When is invoice factoring typically used?</u></b><br>
    •Answer: It is used to improve cash flow when businesses face long customer payment cycles.
</p>

    <p><u><b>4. How does invoice factoring work?</u></b><br>
    •Answer: The business sells invoices to a factor, receives an upfront advance, and the factor collects payment directly from the customer.
</p>

    <p><u><b>5. How much cash is advanced through invoice factoring?</u></b><br>
    •Answer: Typically, 70% to 90% of the invoice value is advanced upfront.
</p>

    <p><u><b>6. Is invoice factoring a loan or a sale?</u></b><br>
    •Answer: Invoice factoring is a sale of receivables, not a traditional loan.
</p>

    <p><u><b>7. What fees are charged in invoice factoring?</u></b><br>
    •Answer: Fees include a factoring or discount fee based on invoice value and collection period.
</p>

    <p><u><b>8. Is collateral required for invoice factoring?</u></b><br>
    •Answer: The invoices themselves act as collateral, so no additional assets are required.
</p>

    <p><u><b>9. Who bears the risk of customer non-payment?</u></b><br>
    •Answer: In non-recourse factoring, the factor bears the risk; in recourse factoring, the business retains the risk.
</p>

    <p><u><b>10. How quickly can funds be received through invoice factoring?</u></b><br>
    •Answer: Funds are often received within 24 to 72 hours after invoice verification.
</p>

    <p><u><b>11. Does invoice factoring affect customer relationships?</u></b><br>
    •Answer: It can, as customers pay the factor directly, but many factors handle collections professionally.
</p>

    <p><u><b>12. What are the benefits of invoice factoring?</u></b><br>
    •Answer: Benefits include improved cash flow, reduced collections burden, and financing based on customer credit quality.
</p>

    <p><u><b>13. What are the risks of invoice factoring?</u></b><br>
    •Answer: Risks include higher costs than bank loans and potential customer perception issues.
</p>

    <p><u><b>14. How does invoice factoring differ from accounts receivable loans?</u></b><br>
    •Answer: Invoice factoring involves selling invoices, while AR loans use invoices as collateral for a loan.
</p>

    <p><u><b>15. When should a business consider invoice factoring?</u></b><br>
    •Answer: A business should consider invoice factoring when it has strong receivables and needs fast working capital.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def factoringinvoicetwelve(request):
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
    Capital Type: Invoice Factoring</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Invoice factoring is best suited for revenue-generating companies from early revenue through growth and mature stages that issue invoices to customers with defined payment terms. This form of financing is not appropriate for pre-revenue companies, as eligibility depends on consistent invoicing and customer payment behavior rather than company age.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
C-Corporations and LLCs are the preferred entity types for invoice factoring, as they support enforceable contracts, clear ownership of receivables, and standardized accounting practices. Sole proprietorships may qualify in limited cases but are generally less favored due to higher perceived risk.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Invoice factoring can be accessed regardless of prior equity or debt funding, since underwriting focuses on the quality of the invoices and the creditworthiness of the company's customers rather than the company's capitalization. Companies with limited operating history may still qualify if customer payment reliability is strong.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Invoice factoring operates within the private asset-based lending and alternative finance market. Providers typically include specialized factoring firms, private credit funds, fintech lenders, and non-bank financial institutions focused on working capital solutions.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
The amount of capital available through invoice factoring is directly tied to the value of outstanding invoices and typically ranges from tens of thousands to several million dollars. Availability fluctuates as new invoices are issued and existing invoices are collected.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Invoice factoring is not considered a capital round and does not involve equity issuance or valuation. It functions as an ongoing working capital facility that converts accounts receivable into immediate cash.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds are disbursed on a rolling basis as invoices are submitted, verified, and approved by the factoring provider. Each invoice effectively represents its own tranche, with advances paid upfront and remaining balances released upon customer payment, net of fees.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Factoring proceeds are commonly used for:
<br>•   Payroll and inventory purchases
<br>•   Vendor payments and operating expenses
<br>•   General working capital needs
Use of funds is generally flexible as long as receivables remain valid and collectible.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk to the factoring provider is primarily related to customer non-payment, while risk to the company includes fees, potential recourse obligations, customer relationship considerations, and concentration risk if receivables are heavily dependent on a small number of customers.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital includes factoring fees, discount rates, and service charges, which are typically higher than traditional bank lines of credit but lower than unsecured short-term debt. Costs reflect speed, flexibility, and credit risk transfer.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are moderate and may include setup fees, legal documentation, due diligence on customers and receivables, and system integration for invoice verification. Costs vary based on invoice volume and complexity.
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
