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


def appscabbage(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Apps</b></u><br>
    Capital Type: Apps i.e. Kabbage</center></p>
    
    <p><b><u>Introduction</u></b><br>
    Since it was formed, the fintech has lent as much as $8 billion and continues to evolve rapidly as it launches new cash flow needs prediction tools <a href="https://fintechmagazine.com/venture-capital/fintech-profile-kabbage-fast-growing-unicorn">(source)</a>. Kabbage approved +209,000 small businesses for $5.8 billion as part of the Paycheck Protection Program, making Kabbage the third largest PPP lender in the U.S. by application volume <a href=" https://finovate.com/category/kabbage/">(source)</a>.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    1) Kabbage offers a streamlined business loan product in the form of a line of credit, which is particularly well-suited for small to medium-sized enterprises seeking flexible funding solutions.

    <br>Unlike traditional term loans that provide a lump sum of money with a fixed repayment schedule, Kabbage's line of credit allows businesses to draw funds up to a pre-approved limit whenever they need it. This flexibility means that businesses only pay interest on the amount they actually use, making it a cost-effective option for managing varying cash flow needs, such as inventory purchases, payroll, or emergency expenses.
    <br>
    <br>The application process for a Kabbage line of credit is conducted entirely online, utilizing an advanced algorithm to analyze real-time data from a variety of sources such as bank accounts, transaction histories, and accounting platforms. This data-driven approach enables Kabbage to provide quick lending decisions, often within minutes.
    <br>
    <br>Once approved, funds can be accessed immediately via the Kabbage dashboard, and the credit line can be reused as repayments are made, providing a revolving facility that adapts to a business's changing financial needs. This model not only simplifies the borrowing experience but also ensures that businesses have continual access to funds as long as they remain creditworthy. (Jr, 2024)
    <br>
    <br>2) Kabbage Funding™ offers access to a commercial line of credit ranging from $2,000 to  $250,000; however, you may be eligible for a larger line of credit based on our evaluation of your business. Each draw on the line of credit will result in a separate installment loan. All loans are subject to credit approval and are secured by business assets. Every loan requires a personal guarantee. Total monthly fees incurred over the loan term range from 2-9% for 6-month loans, 4.5-18% for 12-month loans, 6.75-27% for 18-month loans, and are subject to change for future loans drawn under the available line of credit.  Loans incur a loan fee for each month you have an outstanding balance.  Not all customers will be eligible for the lowest fee. Not all loan term lengths are available to all customers. Eligibility is based on creditworthiness and other factors. Not all industries are eligible for Kabbage Funding. Pricing and line of credit decisions are based on the overall financial profile of you and your business, including history with American Express and other financial institutions, credit history, and other factors. Lines of credit are subject to periodic review and may change or be suspended, accompanied with or without an account closure. (Kabbage Funding™ from American Express Helps Small Businesses Get What’s Needed, When It’s Needed, 2022)
    <br>
    <br>3) Kabbage is one of the most accessible business financing tools in existence. Few online business lenders offer products that are this easy to qualify for. The simplicity of the application process is virtually unrivaled as well. Hardly any paperwork is involved since you can connect your accounts online. And unless you request more than $100,000, you’ll most likely receive your funds in a matter of hours. Thus, if quick and easy are your top priorities, Kabbage may be the best choice.
    <br>
    <br>Another significant advantage of Kabbage is its repayment structure. Many online business lenders require weekly or daily payments, which could put much more pressure on your cash flow than monthly payments.
    <br>
    <br>Lastly, Kabbage’s fee system is a bit complicated, but it is still 100% transparent. Before accepting your offer, you can see your fees and how much you’ll pay every month. The aforementioned fee percentages are readily available on Kabbage’s website. Other business lenders might make you pick up the phone or fill out a brief online form before disclosing this critical information. (Kabbage Funding Review: Pros, Cons & How To Apply, n.d.)
    <br>
    <br>4) Frohwein says Kabbage targets established businesses rather than startups, with its automated model assessing three factors: capacity to repay, character, and the consistency or stability of the business. "We believe we get to know a small business better by being connected to their data sources electronically than any loan officer can do by sitting down at a desk with the borrower," says Frohwein.
    <br>
    <br>He says Kabbage incorporates nontraditional metrics, such as a company's Twitter or Facebook followers, as well as the online reviews its customers post, as a way to round out an applicant's story. "You won't get a loan because you have 7,000 likes on your Facebook page," he says. "But we might increase the cash available to you if you have an active social media following because it establishes the credibility of your business with its customers.” (Dahl, 2021)
    <br>
    <br>5) Some alternatives to Kabbage are LendThrive, Fundbox, OnDeck Capital, BlueVine and Headway Capital. If you need funds to start a new venture, address short-term business needs, or finance your growth plans, it makes the best sense to apply for a loan with any of the Kabbage competitors mentioned above. (5 Kabbage Competitors Offering Amazing Small Business Loans, 2022)
    </p>
                             
    <u><b><p>References</u></b><br>
    5 Kabbage Competitors Offering Amazing Small Business Loans. (2022, March 30). Retrieved from Lend Thrive: <a href="https://lendthrive.com/blog/kabbage-competitors-offering-small-business-loans">https://lendthrive.com/blog/kabbage-competitors-offering-small-business-loans</a>
    <br><br>Dahl, D. (2021, January 8). The Six-Minute Loan: How Kabbage Is Upending Small Business Lending -- And Building A Very Big Business. Retrieved from Forbes: <a href="https://www.forbes.com/sites/darrendahl/2015/05/06/the-six-minute-loan-how-kabbage-is-upending-small-business-lending-and-building-a-very-big-business/">https://www.forbes.com/sites/darrendahl/2015/05/06/the-six-minute-loan-how-kabbage-is-upending-small-business-lending-and-building-a-very-big-business/</a>
    <br><br>Jr, J. F. (2024, July 12). Kabbage Review: Detailed Breakdown, Pros & Cons. Retrieved from Advance Point Capital: <a href="https://advancepointcap.com/blog/kabbage-review/">https://advancepointcap.com/blog/kabbage-review/</a>
    <br><br>Kabbage Funding Review: Pros, Cons & How To Apply. (n.d.). Retrieved from United Capital Source: <a href="https://www.unitedcapitalsource.com/business-loans/lender-reviews/kabbage-funding-review/">https://www.unitedcapitalsource.com/business-loans/lender-reviews/kabbage-funding-review/</a>
    <br><br>Kabbage Funding™ from American Express Helps Small Businesses Get What’s Needed, When It’s Needed. (2022, May 5). Retrieved from American Express: <a href="https://www.americanexpress.com/en-us/newsroom/articles/amex-for-business/kabbage-funding-from-american-express-helps-small-businesses.html">https://www.americanexpress.com/en-us/newsroom/articles/amex-for-business/kabbage-funding-from-american-express-helps-small-businesses.html</a>
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>• Legal Business Entity: Must be a registered entity (LLC, corporation, etc.).
    <br>• Minimum Operational Time: Must be in business for at least one year.
    <br>• Revenue Requirements: Typically, a minimum of $50,000–$100,000 in annual revenue.
    <br>• Active Business Bank Account: Must have an active business checking account.
    <br>• Good Legal Standing: Must be compliant with tax laws and free of legal issues.
    <br>• Personal Guarantee: May be required for some businesses, especially smaller ones.
    <br>• Compliance with Regulations: Must adhere to applicable lending and business regulations.
    <br>• Business Use of Funds: Funds must be used for business-related expenses only.
    <br>• Manageable Debt: The business should not have excessive debt that affects its ability to repay.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Business Identification: EIN, legal structure documents.
    <br>• Financial Records: Bank statements, tax returns, profit and loss statements, balance sheets.
    <br>• Revenue Data: Sales records, transaction history, accounting software data.
    <br>• Personal Identification (for sole proprietors or small businesses): Driver's license or ID, personal guarantee.
    <br>• Business Licenses and Permits: State business license, professional licenses (if applicable).
    <br>• Debt Information: Outstanding debt details and loan terms.
    <br>• Use of Funds Plan: Business plan or statement on capital use.
    <br>• Banking and Payment Account Info: Business checking account and payment platform details.
    <br>• Creditworthiness Information: Credit report consent (optional).
    <br>• Proof of Address: Business address verification.
    </p>
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def appscabbagefaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Apps<br>
    Capital Type: Apps (i.e. Kabbage)</center></p>                        
    <p><center><u><b>Frequently Asked Question for Kabbage</u></b></center></p>
    <p><u><b>1. What is Kabbage and how does it work?</u></b><br>
    • Answer: Kabbage is an online lending platform that provides businesses with quick access to working capital through a revolving line of credit. The application process is streamlined and can be done entirely online, offering flexible loan terms.
    </p>
                             
    <p><u><b>2. How quickly can I get access to funds through Kabbage?</u></b><br>
    • Answer: One of the main advantages of using Kabbage is the speed. Once approved, funds can typically be available in your account as soon as the same day or within a few days, depending on the specific terms.
    </p>
                             
    <p><u><b>3. What are the eligibility requirements to use Kabbage?</u></b><br>
    • Answer: Kabbage typically requires that your business has been operating for at least one year and has a minimum of $50,000 in annual revenue. However, the exact requirements can vary, so it’s important to check the specific criteria when applying.
    </p>
                             
    <p><u><b>4. What types of businesses can use Kabbage?</u></b><br>
    • Answer: Kabbage is suitable for a wide range of small and medium-sized businesses, including retail, manufacturing, and service-based industries. The platform is designed to cater to businesses in need of working capital, especially those that may not qualify for traditional bank loans.</p>
                             
    <p><u><b>5. How is my creditworthiness evaluated?</u></b><br>
    • Answer: Unlike traditional lenders, Kabbage looks at real-ti me data from your business, such as your revenue, cash flow, and other financial factors, rather than just your personal credit score. This means that businesses with less-than-perfect credit may still be able to qualify for funding.
    </p>
                             
    <p><u><b>6. Are the interest rates competitive?</u></b><br>
    • Answer: Interest rates on Kabbage lines of credit are generally considered competitive for businesses in need of quick access to capital. However, rates can vary based on your specific financial situation, the amount of capital requested, and how much you borrow.</p>
                             
    <p><u><b>7. What fees are associated with Kabbage?</u></b><br>
    • Answer: Kabbage charges a monthly fee based on the outstanding balance of the loan. It's important to carefully review the terms and understand any fees that may apply before committing to a loan.</p>
                             
    <p><u><b>8. How much funding can I get from Kabbage?</u></b><br>
    • Answer: Kabbage offers lines of credit ranging from $1,000 to $250,000, depending on your business’s financial profile. The exact amount you’re eligible for will be determined by factors such as revenue and the length of time in business.</p>
                             
    <p><u><b>9. What are the repayment terms like?</u></b><br>
    • Answer: Kabbage offers flexible repayment options, typically on a monthly or weekly basis, depending on your revenue cycle. Repayments are based on your business's cash flow, making it easier to manage repayments.</p>
                             
    <p><u><b>10. Can I use Kabbage for any business purpose?</u></b><br>
    • Answer: Yes, Kabbage allows businesses to use the funds for a variety of purposes, such as purchasing inventory, covering operating expenses, managing payroll, or expanding operations.</p>
                             
    <p><u><b>11. How does using Kabbage compare to traditional bank loans?</u></b><br>
    • Answer: Kabbage is often faster and easier to access than traditional bank loans. Unlike banks, Kabbage has a more flexible approach to lending and doesn’t require extensive paperwork or collateral. However, bank loans may offer lower interest rates for businesses with strong credit.</p>
                             
    <p><u><b>12. Is the application process difficult?</u></b><br>
    • Answer: The application process with Kabbage is relatively simple and can be completed online in a matter of minutes. You’ll need to connect your business’s financial accounts, such as your accounting software or bank account, to provide Kabbage with data to assess your eligibility.
    </p> 
                             
    <p><u><b>13. Can I use Kabbage if I have a less-than-perfect credit score?</u></b><br>
    • Answer: Yes, one of the advantages of Kabbage is that it doesn’t rely heavily on your personal credit score. Kabbage uses alternative data sources, such as your business's financial performance, to determine eligibility, so businesses with poor credit history may still be approved.</p>
    
    <p><u><b>14. Can I access more funding over time?</u></b><br>
    • Answer: Yes, once you’ve paid down your balance, you may be eligible to borrow more from Kabbage. Your credit limit may be adjusted based on your business’s performance and payment history.</p>
    
    <p><u><b>15. What makes Kabbage a good option for raising capital?</u></b><br>
    • Answer: Kabbage is ideal for businesses that need quick, flexible funding without the traditional hurdles of applying for a bank loan. It’s particularly useful for businesses with variable cash flows, those looking to manage short-term working capital needs, or businesses that may not qualify for traditional financing options.</p>
    
    <p><u><b>16. Is Kabbage secure and trustworthy?</u></b><br>
    • Answer: Yes, Kabbage is a reputable company with strong security protocols in place to protect your financial data. The platform uses encryption and secure connections to ensure the safety of sensitive business information.</p>
    
    <p><u><b>17. What happens if I can’t make a repayment on time?</u></b><br>
    • Answer: Kabbage understands that cash flow can sometimes be unpredictable. If you miss a payment, it’s important to contact their customer service team to discuss your options. Late fees may apply, but they’re often more flexible than traditional lenders in working with businesses facing financial difficulties.</p>
    
    <p><u><b>18. Is Kabbage a good option for growing my business?</u></b><br>
    • Answer: If your business needs quick, short-term capital to cover expenses, invest in inventory, or take advantage of growth opportunities, Kabbage can be a good option. Its fast application process and flexible terms make it a solid choice for businesses looking to scale quickly.</p>     
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def appscabbagetwelve(request):
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
    Apps i.e. Kabbage</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    The ideal stage for using apps like Kabbage is when a business is past the very early startup phase but may not yet be large enough or well-established enough to secure traditional bank loans. These businesses typically need flexible, quick access to capital, have some revenue history, and might face variable cash flow challenges or temporary capital needs.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    The most ideal entity types for using apps like Kabbage are Limited Liability Companies (LLCs), Corporations, Sole Proprietorships, Partnerships, and Limited Liability Partnerships (LLPs). These businesses are typically established with at least one year of operations and consistent revenue. LLCs and Corporations often have a clearer financial structure, making it easier to qualify for larger lines of credit, while Sole Proprietorships and Partnerships can still access funding as long as they demonstrate strong cash flow and financial viability.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    There aren't specific restrictions based solely on how much pre-capital a business has raised before using apps like Kabbage. However, the platform will assess the business’s financial health, revenue, and cash flow, regardless of past funding. Businesses with significant existing debt or complicated investor structures may face additional scrutiny. The key focus for Kabbage is whether the business has the ability to repay the loan based on its current operations.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    Although there are no direct restrictions, there are some limitations based on how companies have raised pre-capital that could interfere with using apps like Kabbage and they usually stem from existing debt obligations or investor agreements. These could include restrictions on borrowing due to investor-imposed covenants or high levels of existing debt, which make it harder for a business to qualify for additional loans. 
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    A business can raise between $1,000 and $250,000 through Kabbage, with the specific limit determined by factors such as revenue, time in business, financial health, and credit history.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    The ideal capital round for a company that wants to use Kabbage is typically post-seed or Series A, as these stages usually involve businesses that have some operational history, established revenue, and are looking for short-term, flexible financing to manage cash flow and fund growth. Kabbage’s ability to provide fast, revolving credit lines makes it well-suited for companies that need quick access to capital but might not yet qualify for traditional, larger-scale loans.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Unlike traditional funding rounds or investments where capital is often raised in distinct "tranches" or stages, apps like Kabbage typically don't operate on a tranche-based system for lending. Instead, Kabbage provides lines of credit with revolving terms, meaning businesses can borrow up to an approved limit and repay based on their cash flow needs, essentially borrowing and repaying in an ongoing cycle. 
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Businesses using funds from Kabbage can generally use the money for working capital, payroll, inventory, marketing, expansion, and other business-related expenses. The main restriction is that funds must be used exclusively for business purposes, not for personal expenses or activities outside of the business.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    A business using Kabbage should have a moderate level of risk tolerance, as the platform provides quick access to credit for short-term financial needs, but it also requires businesses to manage their cash flow, understand the fee structure, and make timely repayments. The risks primarily involve cash flow fluctuations, debt management, and potential repayment challenges if revenue doesn't meet expectations. 
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    A business using Kabbage should have a moderate level of capital cost tolerance, meaning they must be comfortable with the higher fees associated with short-term, revolving credit lines. While the platform offers quick access to funds and flexible repayment, the cost of capital can be higher than traditional financing options. </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    The upfront costs of using Kabbage are generally very low or nonexistent, as there are no application or origination fees. The main costs come after the line of credit is accessed and are tied to the monthly fees on the borrowed amount. These fees typically range from 1.5% to 10% per month, depending on the business’s financial profile. 
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    Businesses can get capital quickly through Kabbage, often receiving funds within minutes to a few hours after approval. The entire process—from application to fund availability—is streamlined, and the speed of accessing capital is one of the main advantages for businesses needing fast access to working capital. If you have your financial data linked to Kabbage, you can sometimes get access to funds the same day you apply.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)