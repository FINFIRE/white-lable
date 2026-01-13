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
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Factoring</b></u><br>
    Capital Type: Accounts Receivable Loans</center></p>
    
    <p><b><u>Introduction</u></b><br>
    Accounts Receivable (AR) Loans are ideal for companies needing fast access to 70% to 80% of their outstanding invoice amounts. By using unpaid invoices as collateral, businesses can cover the gap between providing products or services and receiving customer payments. However, while AR financing provides quick access to working capital, it can be expensive. This type of financing is ideal for companies like {name}, who need the immediate cash flow. Accounts Receivable Loans have played a crucial role in business financing since the early 1300s. For example, the global accounts receivable financing market size was valued at approximately $400 billion USD in 2023. Growing at a compound annual growth rate (CAGR) of 6%, (AR) loans are projected to reach about $700 billion USD by 2032. In 2024, nearly 50% of business-to-business (B2B) invoices were overdue. This highlights the importance of accounts receivable (AR) financing to help businesses manage cash flow and keep operations running smoothly.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br>1. Accounts receivable and inventory financing (ARIF) is the most fundamental form of collateral-based commercial lending. It combines elements of secured lending and short-term business loans. Commercial borrowers use the value of their receivables and inventory, or working assets, as collateral to secure financing to produce and market their products and services. (OCC n.d.)
<br>
    <br>2. Accounts Receivable (AR) relationships generally involve high risk. Borrowers often seek AR when they are unable to secure other forms of financing due to weaker financial standing, operating in volatile or seasonal industries, or undergoing rapid growth. These borrowers typically face higher default risks, including high leverage, inconsistent or low profitability, limited working capital and cash reserves, and fluctuating collateral values that can decline quickly. (OCC n.d.)
<br>
    <br>3. Accounts receivable financing is one of the oldest forms of financing, historically used in England for deals involving clothing and grain. Factoring allowed producers to receive immediate payment for goods that needed to be transported over long distances, rather than waiting until delivery for payment.
<br>
    <br>Today, accounts receivable financing remains a popular solution for businesses seeking to improve cash flow and support growth. It is especially common in industries like oil and gas, telecom, trucking, staffing, pipeline, and healthcare, where customers often have payment terms ranging from 30 to 90 days, creating cash flow gaps that need to be bridged. (Andrews 2024)
<br>
    <br>4. Accounts Receivable (AR) financing can be expensive due to the fees and interest rates charged by lenders. These costs often include a factoring fee, typically ranging from 1% to 5% of the invoice value, and additional interest charges, which can quickly accumulate. Unlike traditional loans, AR financing is short-term and provides immediate cash, but the combined fees and rates can significantly reduce a company's profit margins. For businesses that frequently use this form of financing, the high costs can add up over time, making it a less affordable option in the long run.
<br>
    <br>5. To qualify for accounts receivable financing, lenders focus on factors like consistent invoice volume, the creditworthiness of your customers, and minimum revenue requirements, which vary by lender. While business age is less critical than with traditional loans, many lenders prefer companies that have been operating for at least a year. Certain industries, due to their reliable invoicing practices and client payment behavior, are also more favorable for this type of financing.
    </p>
                             
    <u><b><p>References</u></b><br>
    <br>Accounts receivable and inventory financing. (n.d.). OCC.gov. <a href="https://www.occ.treas.gov/topics/supervision-and-examination/credit/commercial-credit/accounts-receivable.html">https://www.occ.treas.gov/topics/supervision-and-examination/credit/commercial-credit/accounts-receivable.html</a>
    <br><br>Katie.Andrews. (2024, May 6). Accounts Receivable Financing History | Scale Funding. Scale Funding. <a href="https://getscalefunding.com/scale-funding-insights/history-of-accounts-receivable-financing/">https://getscalefunding.com/scale-funding-insights/history-of-accounts-receivable-financing/</a>
    <br><br>Dataintelo, Sharma, R., & Dataintelo. (2025, January 7). Accounts Receivable Financing Market Research Report 2032. Dataintelo. <a href="https://dataintelo.com/report/accounts-receivable-financing-market">https://dataintelo.com/report/accounts-receivable-financing-market</a>
    <br><br>13 Accounts Receivable Stats you should know in 2024. (n.d.). 13 Accounts Receivable Stats You Should Know in 2024. <a href="https://upflow.io/blog/ar-collections/13-accounts-receivable-cash-collection-statistics-2024">https://upflow.io/blog/ar-collections/13-accounts-receivable-cash-collection-statistics-2024</a>
    <br><br>Clarify Capital. (2024, January 9). Accounts Receivable Financing: best options, How it works. <a href="https://clarifycapital.com/blog/accounts-receivable-financing#:~:text=Qualifying%20for%20Accounts%20Receivable%20Financing,invoicing%20practices%20and%20client%20reliability">https://clarifycapital.com/blog/accounts-receivable-financing#:~:text=Qualifying%20for%20Accounts%20Receivable%20Financing,invoicing%20practices%20and%20client%20reliability.</a>
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>• Legally Registered Business - The business must be a legally registered entity (LLC, corporation, or sole proprietorship) and in good standing with all necessary regulatory bodies.
    <br>• Ownership of Receivables - The business must own the accounts receivables it seeks to finance. The receivables must be free of liens or claims by other creditors, meaning no other party has a legal right to collect on them.
    <br>• Valid and Enforceable Invoice - Invoices presented for financing must be legitimate, meaning they represent completed sales or services that have been fully delivered. The goods or services provided must meet the agreed-upon terms with the customer, and there should be no disputes or legal issues over the receivables.
    <br>• Creditworthy Customers - The customers responsible for paying the receivables need to have a reliable payment history and be creditworthy. Lenders often check the credit ratings of these customers to reduce the risk of default.
    <br>• Assignment of Receivables - The business may be required to legally assign the receivables to the lender, giving the lender the right to collect payment directly from the customers if needed.
    <br>• Compliance with Laws - The business and its receivables must comply with all relevant federal, state, and local laws. This includes industry-specific regulations, tax obligations, and contractual obligations that govern the sales or services provided.
    <br>• No Existing Liens on Receivables - The receivables used as collateral must be unencumbered, meaning they are not pledged as collateral to another creditor or lender. The lender usually conducts a lien search to confirm this.
    <br>• No Insolvency or Bankruptcy - The business must not be in bankruptcy or insolvency proceedings. Businesses in financial distress may not qualify for AR financing due to the high risk involved.
    <br>• Contractual Representations and Warranties - The borrower may be required to make certain representations and warranties in the financing agreement, such as the validity of the receivables, the creditworthiness of customers, and the company’s financial stability.
    <br>• Non-Recourse vs. Recourse Financing Terms - The terms of the financing can be structured as recourse or non-recourse. In recourse financing, the business remains liable if the customer does not pay the invoice. In non-recourse financing, the lender assumes the risk of non-payment by the customer.
    <br>• Audit Rights - Lenders may reserve the right to audit the business’s accounts receivable records to verify the validity of the receivables and the business’s financial condition.
    <br>• Minimum Revenue and Business Age - Lenders may impose minimum revenue thresholds to ensure the business has consistent activity to justify financing. Additionally, some lenders prefer businesses that have been operational for at least a year.
    <br>• Industry Type - Certain industries are more favorable for AR loans due to predictable cash flow and invoicing practices. Businesses in industries like healthcare, manufacturing, transportation, and staffing are typically viewed as more reliable.
    <br>• No Default on Previous Financing - If the business has prior financing arrangements, it should not be in default. Defaulting on other loans may disqualify the business from obtaining new AR financing.
    <br>•  Insurance Coverage (Optional) - In some cases, lenders may require the business to have adequate insurance coverage, particularly for industries where the delivery of goods or services carries higher risks.
    <br>• Contracts with Customers - Lenders may require the business to have written agreements or contracts with its customers that clearly outline the terms of payment and the goods or services provided. This ensures the invoices are enforceable.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>1. Accounts Receivable Documents
        <br>• Accounts Receivable Aging Report: Detailed report showing outstanding invoices by age (e.g., current, 30, 60, 90+ days).
        <br>• Copies of Invoices: Copies of specific invoices to be used as collateral in the AR financing agreement.
        <br>• Sales Contracts or Agreements: Contracts between the business and customers verifying terms of sales or services.
        <br>• Proof of Delivery or Completion: Documentation proving delivery or completion of services (e.g., delivery receipts, signed acceptance forms).
        <br>• Accounts Receivable Insurance (if applicable): Proof of AR insurance to protect against customer non-payment.
    <br><br>2. Company Financials
        <br>• Financial Statements: Recent Balance Sheet, Income Statement (Profit & Loss), and Cash Flow Statement to assess financial health.
        <br>• Business Tax Returns: Copies of tax returns for the past two or three years to verify revenue and expenses.
        <br>• Bank Statements: Recent bank statements (past 3-6 months) showing cash flow, deposits, and obligations.
        <br>• Accounts Payable Aging Report: A report showing amounts owed to suppliers and vendors for a full financial picture.
        <br>• Debt Schedules: A detailed list of current debts or loans, including repayment schedules.
    <br><br>3. Business and Legal Documents
        <br>• Articles of Incorporation or Business Registration: Proof that the business is legally registered and in good standing.
        <br>• UCC Lien Filings: Information on any existing Uniform Commercial Code filings that affect the receivables, especially if pledged as collateral elsewhere.
        <br>• Insurance Documentation: General business insurance documents, particularly if specific coverage is required for assets or invoices.
    <br><br>4. Personal and Credit Information
        <br>• Credit Reports: Credit reports for the company, and potentially the individual business owners.
        <br>• Personal Identification and Business Ownership: Documents such as driver's licenses or passports of the owners, and proof of business ownership or shareholder agreements.
        <br>• Personal Financial Statements (if applicable): Personal financial statements from owners if a personal guarantee is required.
    <br><br>5. Customer Payment History
        <br>• Customer Payment History: Records of payment histories from key customers to verify payment patterns and reliability.
    </p>
        """)
    
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
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,name=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def factoringaccountsreceivablefaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Factoring<br>
    Capital Type: Accounts Receivable Loans</center></p>                        
    <p><center><u><b>Frequently Asked Question for Accounts Receivable Loans</u></b></center></p>
    <p><u><b>1. What are accounts receivable loans?</u></b><br>
    • Answer: An accounts receivable loan is a type of financing where a business uses its outstanding invoices (receivables) as collateral to secure immediate cash. The lender advances a percentage of the receivables' value, allowing the business to access funds before its customers pay their invoices.
    </p>
                             
    <p><u><b>2. How does AR financing work?</u></b><br>
    • Answer: With AR financing, a company sells or pledges its outstanding invoices to a lender. The lender provides a cash advance, typically 70% to 90% of the total invoice value. Once the customer pays the invoice, the lender deducts fees and returns the remaining balance to the business.
    </p>
                             
    <p><u><b>3. What are the benefits of AR loans?</u></b><br>
    • Answer: 
    <br>- Improved Cash Flow: Provides immediate access to funds tied up in unpaid invoices.
    <br>- No Equity Dilution: Does not require the business to give up ownership or control.
    <br>- Quick Access to Funds: Funding can be obtained within 24-48 hours.
    <br>- Flexible Terms: Can be used as needed based on the company's receivables.
    </p>
                             
    <p><u><b>4. What are the typical costs associated with AR loans?</u></b><br>
    • Answer:The costs typically include a factoring fee or interest rate that ranges from 1% to 3% per month, depending on the lender, the size of the loan, and the creditworthiness of your customers. There may also be administrative or setup fees.</p>
                             
    <p><u><b>5. How much funding can a business get through AR loans?</u></b><br>
    • Answer: The amount of funding depends on the total value of the outstanding invoices. Lenders typically advance between 70% and 90% of the receivables’ value, with the remaining balance released once the invoices are paid.
    </p>
                             
    <p><u><b>6. How long does it take to receive funds?</u></b><br>
    • Answer: Once approved, businesses can receive funds within 24 to 48 hours, making AR loans a fast way to address cash flow needs.
    </p>
                             
    <p><u><b>7. What types of businesses can benefit from AR loans?</u></b><br>
    • Answer: AR loans are ideal for businesses that sell goods or services on credit and have customers who take time to pay. This includes manufacturing, wholesale, distribution, staffing, and service-based companies that experience cash flow gaps due to long payment cycles.</p>
                             
    <p><u><b>8. Do customers need to know about the AR loan?</u></b><br>
    • Answer: In many cases, yes. Some AR financing arrangements involve notifying customers that their invoices have been financed, especially in factoring agreements where the lender collects payments directly. In other types of AR loans (asset-based lending), the business may continue collecting payments without customer involvement.
    </p>
                             
    <p><u><b>9. What happens if a customer doesn’t pay an invoice?</u></b><br>
    • Answer: If a customer doesn’t pay an invoice, the lender may hold the business responsible for repaying the advanced amount. Some lenders offer "non-recourse" financing, meaning the lender takes on the risk of non-payment, but this typically comes with higher fees.</p>
                             
    <p><u><b>10. What is the difference between factoring and accounts receivable loans?</u></b><br>
    • Answer: Factoring involves selling receivables to a lender, who collects the payments directly from customers. AR loans, on the other hand, use receivables as collateral, allowing the business to retain control over customer relationships and collections while borrowing against the invoices.</p>
                             
    <p><u><b>11. What credit score is required for an AR loan?</u></b><br>
    • Answer: Lenders focus more on the creditworthiness of the business’s customers than the business itself. A good history of reliable, paying customers is more important than the business owner’s credit score.</p>
                             
    <p><u><b>12. Is AR financing a long-term solution?</u></b><br>
    • Answer: AR loans are generally used as a short-term financing solution to manage cash flow or fund growth. They are not typically meant for long-term capital needs, as the costs can add up over time.
    </p> 
                             
    <p><u><b>13. Can startups use accounts receivable loans?</u></b><br>
    • Answer: Yes, startups that generate invoices for customers can use AR loans, but they need a consistent stream of receivables from creditworthy customers. Lenders may be more cautious when working with newer businesses with limited operating history.</p>

    <p><u><b>14. How is AR loan eligibility determined?</u></b><br>
    • Answer:     
    <br>- Lenders evaluate several factors, including:
    <br>- The value and age of the receivables.
    <br>- The creditworthiness and payment history of customers.
    <br>- The business’s financial health.
    <br>- The industry and stability of the business.</p>
    
    <p><u><b>15. Can AR loans be combined with other forms of financing?</u></b><br>
    • Answer: Yes, AR loans can often be combined with other financing options like traditional business loans, lines of credit, or equity funding, depending on the company's needs and its lender’s terms.</p>

    <p><u><b>16. What happens after a business repays the loan?</u></b><br>
    •Answer: Once a customer pays the invoice, the lender deducts fees from the repayment and returns the remaining balance to the business. The business can continue to use AR financing as needed for future receivables.</p>                      
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR</b></u><br>
    Capital Type: Accounts Recievable Loans</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    While {n} is in the growth stage, it is ideal to use accounts receivable loans to quickly finance expansion and improve cash flow. As the company grows, it may face increased demand for products or services, requiring additional capital to scale operations, hire more staff, invest in inventory, or enhance infrastructure. Accounts Receivable loans solve those problems.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Accounts receivable financing is a good option for LLCs, C Corporations, and S Corporations alike. It allows these entities to secure quick capital without giving up equity or control, making it an ideal financing solution for companies like {n}, who are focused on operational growth and cash flow management.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    Since  {n} has already raised {preraise} in pre-capital, utilizing AR financing could be a strategic way to bridge any cash flow gaps while continuing to scale operations. The pre-capital could be used to support initial expansion, and AR financing would provide ongoing liquidity to keep operations running smoothly during periods of growth.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    With {preraise} in pre-capital raised through a {premarket}, AR financing is a logical next step that provides immediate cash flow to fuel expansion and growth without waiting for customer payments. It enables  {n} to keep funds circulating in the business while avoiding additional equity dilution.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    AR financing is typically used for short-term cash flow needs and doesn't involve a large amount of capital. This aligns well with  {n}’s goal of raising immediate working capital (e.g., $100,000 to $500,000), as AR financing is based on the value of current receivables and can be customized to meet specific needs.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Since {n} is in its {rounds} Round of capital raising, AR loans offer an effective complement to equity financing. These loans can help the company manage cash flow while other capital sources are being finalized, allowing {n} to meet operational needs without taking on additional debt or diluting ownership.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    AR loans offer flexibility in how capital is deployed. For {n}, this means the company can access the funds in tranches as invoices are issued. This incremental funding ensures that {n} maintains healthy cash flow while scaling its operations without needing to wait for full payment from customers.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    AR loans offer flexibility with how the funds can be used. {n} can use the capital to cover various expenses, including:
    <br>1. Startup working capital
    <br>2. Growth scalability
    <br>3. Cash flow management
    <br>4. Hiring and human capital expansion
    <br>5. Other operational needs
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Since AR financing relies on the company’s receivables, there is a large risk that the company’s customers may not pay on time or in full, which can affect the company’s ability to repay the loan. However, the risk is mitigated by securing funding against invoices that are deemed reliable and collectible. AR financing is generally suitable for companies with a stable customer base and predictable cash flows.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    While AR loans come with factoring fees (usually between 1% to 3% per month), {n}’s tolerance for capital costs will allow it to manage these expenses. The quick access to liquidity provides the company with an opportunity to reinvest in its growth and meet operational needs without waiting for customers to pay their invoices.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    The upfront costs for AR financing are typically low compared to other financing options. {n} will need to pay minimal fees for application processing and due diligence. The costs are generally structured as a percentage of the amount borrowed, and the company may need to pay for initial setup, legal agreements, and transaction fees, which could range from $1,000 to $5,000 depending on the lender.  
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    AR financing is one of the quickest financing methods available. Once {n} establishes a relationship with a financing provider, it can receive capital in as little as 24 to 48 hours, depending on the lender’s process and the quality of the receivables. This timeline is ideal for businesses needing quick access to funds to keep operations running smoothly during periods of growth.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)