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


def smallbusinessadministrationexpress(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Small Business Administration</b></u><br>
    Capital Type: Express Loan</center></p>
    
    <p><b><u>Introduction</u></b><br>
    For the 2024 fiscal year, SBA 7(a) lenders approved over 70,000 loans for a total of $31.1 billion in small business loans, according to the weekly SBA lending report. On average, business owners were granted $443,097 per SBA loan to grow their businesses. Over 22,000 approvals were for brand-new startups and startup businesses with less than two years under their belts. Most startups received 7(a) SBA loans, while more than 1,000 startups obtained 504 financing <a href="https://www.bankrate.com/loans/small-business/sba-loan-top-lenders/">(source)</a>.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    1) An SBA Express loan is a small-business loan that is partially guaranteed by the U.S. Small Business Administration and issued by banks and other approved lenders. These loans are part of the SBA 7(a) program but have lower borrowing maximums and faster funding times than standard 7(a) loans. Like other SBA loans, Express loans are a great funding choice for small businesses because they offer competitive interest rates and flexible repayment terms. (Rick Lane, 2024)

    <br><br>2) The 7(a) loan program is SBA's primary program for providing financial assistance to small businesses. The SBA Express allows certain lenders to generally use their own processes and procedures in exchange for a lower SBA guaranty percentage. SBA Express lenders have delegated authority to process, close, service, and liquidate the 7(a) loan without SBA review. (Types of 7(a) loans, 2024)

    <br><br>3) An SBA Express loan is a working capital loan of $500,000 designed for small businesses. It is part of the 7(a) loan program. But unlike other loans offered through the 7(a) program, Express loans are faster business loans that can be funded within a few weeks.

    <br><br>Because Express loans don’t require direct SBA approval, lenders can follow their normal process for evaluating the loan. This streamlined process helps small businesses get approved for this loan more quickly than other SBA loans.

    <br><br>The amount you can borrow is limited to $500,000 or less, but you can use your funding for a variety of expenses, including working capital, expansion, equipment and debt refinancing. The amount the SBA guarantees is lower than its normal 7(a) loans, which only affects the lender’s decision-making for approving the loan. But for businesses that only need a small amount, they can be a handy way to get quick funding. (Guinan, 2024)
    </p>
                             
    <u><b><p>References</u></b><br>
    Guinan, K. (2024, Novmeber 12). SBA Express loan: What it is and how to apply. Retrieved from Bankrate : <a href="https://www.bankrate.com/loans/small-business/sba-express-loan/">https://www.bankrate.com/loans/small-business/sba-express-loan/</a>

    <br><br>Rick Lane, R. K. (2024, September 11). SBA Express Loan: What It Is and How to Apply. Retrieved from Nerd Wallet: <a href="https://www.nerdwallet.com/article/small-business/sba-express-loans">https://www.nerdwallet.com/article/small-business/sba-express-loans</a>

    <br><br>Types of 7(a) loans. (2024, December 5). Retrieved from SBA: <a href"https://www.sba.gov/partners/lenders/7a-loan-program/types-7a-loans">https://www.sba.gov/partners/lenders/7a-loan-program/types-7a-loans</a>
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>• Be an operating, for profit business located in the U.S.
    <br>• Be small under SBA Size Requirements1
    <br>• Not be a type of ineligible business 2
    <br>• Be creditworthy and demonstrate a reasonable ability to repay the loan
    <br>• Credit Score: Although the SBA itself doesn’t set an official minimum credit score, most lenders require a credit score of 650 or higher. In some cases, depending on the loan size and lender, a score as high as 680 or 700 may be necessary.
    <br>• Business Credit: For smaller loan amounts, typically under $500,000, lenders use the FICO Small Business Scoring Service (SBSS). A score of 155 or higher is usually required to pass this screening. While some lenders may review traditional business credit scores, such as D&B’s Paydex score, these are not required for SBA 7(a) loan applications.
    <br>• Good Character: Borrowers must pass a background check, and a criminal history—particularly financial-related offenses—may affect eligibility.
    <br>• Demonstrated Need for Credit: Applicants must demonstrate they cannot secure credit from other sources on reasonable terms, documenting previous loan attempts and rejections.
    <br>• Business Plan: A clear and feasible business plan is essential for showing how the loan will support business operations and growth.
    <br>• No Government Debt: Borrowers must not be delinquent on any federal loans, such as existing SBA loans or federal tax debts.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• SBA Form 1919: Borrower Information Form (required for all applicants).
    <br>• SBA Form 912: Statement of Personal History (required for principal owners).
    <br>• SBA Form 413: Personal Financial Statement.
    <br>• Legal business registration documents (e.g., articles of incorporation)
    <br>• Lease agreements (if applicable)
    <br>• Financial statements for the last three years (including income statements, balance sheets, and cash flow statements)
    <br>• Three years of business and personal tax returns
    <br>• Current profit & loss (P&L) statements and balance sheets
    <br>• Details of present debt obligations
    <br>• A detailed schedule of any collateral you are offering
    <br>• Resumes for all business owners.
    </p>
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def smallbusinessadministrationexpressfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Small Business Administration<br>
    Capital Type: Express Loan</center></p>                        
    <p><center><u><b>Frequently Asked Question for Express Loan</u></b></center></p>
    <p><u><b>1. What is an SBA Express Loan, and how is it different from other SBA loans?</u></b><br>
    • Answer: An SBA Express Loan is a type of 7(a) loan, but it offers a faster approval process (typically within 36 hours) and a streamlined application compared to the regular SBA 7(a) loan. While SBA 7(a) loans generally offer higher loan amounts and longer repayment terms, SBA Express Loans are designed to meet smaller, short-term financing needs more quickly, with loan amounts up to $500,000.</p>
                             
    <p><u><b>2. How quickly can I receive an SBA Express Loan?</u></b><br>
    • Answer: The SBA Express Loan process is much faster than traditional SBA loans. Approval can happen within 36 hours, and funds can be disbursed in as little as a few days, making it an ideal option for businesses that need quick access to capital.</p>
                             
    <p><u><b>3. What are the primary uses of an SBA Express Loan?</u></b><br>
    • Answer: SBA Express Loans can be used for working capital, inventory purchases, equipment, business expansion, or refinancing existing debt. They are meant for short-term financing needs rather than long-term projects or speculative investments.</p>
                             
    <p><u><b>4. What is the maximum loan amount for an SBA Express Loan?</u></b><br>
    • Answer: The maximum loan amount for an SBA Express Loan is $500,000. This is ideal for businesses needing smaller amounts of capital without going through the lengthy approval processes required for larger SBA loans.</p>
                             
    <p><u><b>5. Who is eligible for an SBA Express Loan?</u></b><br>
    • Answer: Eligible businesses must:
    <br>- Be a for-profit business operating in the U.S.
    <br>- Meet size standards set by the SBA (e.g., revenue and employee limits).
    <br>- Demonstrate the ability to repay the loan.
    <br>- Have a good credit history and financial stability.
    <br>- In most cases, businesses must also be in business for at least two years (though startups may still be eligible depending on other factors).
    </p>
                             
    <p><u><b>6. What are the eligibility requirements for the business owner?</u></b><br>
    • Answer: Business owners must generally have:
    <br>- U.S. citizenship or legal residency.
    <br>- A good personal credit score (typically 650 or higher).
    <br>- The ability to personally guarantee the loan (for most SBA loans, including Express).
    <br>- The company must have sound financials and the ability to demonstrate the ability to repay the loan.</p>
                             
    <p><u><b>7. What are the interest rates and fees for an SBA Express Loan?</u></b><br>
    • Answer: SBA Express Loan interest rates are typically market-driven, but they are capped by the SBA. The rate is usually the prime rate plus 6.5% (or lower, depending on the lender). Additional fees may include an origination fee, which typically ranges from 0.25% to 3%, depending on the loan size.</p>
                             
    <p><u><b>8. What is the repayment term for an SBA Express Loan?</u></b><br>
    • Answer: The repayment term for an SBA Express Loan can be up to 10 years, but typically, the repayment period is shorter depending on the loan’s purpose (e.g., equipment purchases may have shorter repayment terms). The SBA generally allows for flexible repayment terms, which helps businesses manage cash flow better.</p>
                             
    <p><u><b>9. Can I use an SBA Express Loan to refinance debt or pay off other loans?</u></b><br>
    • Answer: Yes, you can use an SBA Express Loan to refinance certain types of business debt, such as high-interest loans or lines of credit. However, the SBA has specific guidelines on what types of debt can be refinanced, and it cannot be used for personal debt refinancing.</p>
                             
    <p><u><b>10. What collateral do I need to provide for an SBA Express Loan?</u></b><br>
    • Answer: SBA Express Loans generally do not require collateral for loans under $25,000. For loans above this amount, the lender may request collateral, though the SBA allows for flexibility in collateral requirements. Personal guarantees from business owners are often required, especially for larger loans.</p>
                             
    <p><u><b>11. How does an SBA Express Loan compare to a traditional bank loan?</u></b><br>
    • Answer: SBA Express Loans are generally easier to qualify for than traditional bank loans, particularly for businesses that might have less-than-perfect credit or limited operating history. They also offer faster approval times (36 hours) and longer repayment terms than many conventional loans. However, they may require personal guarantees and come with slightly higher interest rates compared to some conventional loans.</p>
                             
    <p><u><b>12. Can I use an SBA Express Loan for business expansion or hiring employees?</u></b><br>
    • Answer: Yes, an SBA Express Loan can be used for business expansion needs, including hiring new employees, opening a new location, or purchasing equipment. This type of loan is ideal for businesses in their growth stage that need capital to scale quickly.
    </p> 
                             
    <p><u><b>13. What is the difference between an SBA Express Loan and an SBA 7(a) Loan?</u></b><br>
    • Answer: The SBA 7(a) Loan is the most common type of SBA loan and offers larger loan amounts (up to $5 million) and longer repayment terms (up to 25 years). In contrast, the SBA Express Loan is designed for smaller, short-term needs with a quicker approval process and a lower maximum loan amount of $500,000.</p>

    <p><u><b>14. What happens if my SBA Express Loan application is denied?</u></b><br>
    • Answer: If your application is denied, you will receive an explanation from the lender about why it was declined. Common reasons include insufficient cash flow, a poor credit history, or a failure to meet the SBA’s eligibility requirements. In some cases, you may be able to reapply after addressing the issues raised or provide additional documentation.</p>
    
     <p><u><b>15. How does an SBA Express Loan compare to other types of financing options (e.g., credit cards, lines of credit, or venture capital)?</u></b><br>
    • Answer: An SBA Express Loan is a lower-cost option compared to credit cards or lines of credit, which often have higher interest rates. It’s also a non-dilutive form of financing (meaning you don’t give up equity in your company), unlike venture capital. It offers fixed repayment terms and is a better option for businesses that need quick capital for short-term needs but want a more affordable financing solution than high-interest alternatives.</p>
    
    <p><u><b>16. Can a business use an SBA Express Loan more than once?</u></b><br>
    • Answer: Yes, a business can apply for an SBA Express Loan multiple times, as long as the loan is repaid according to the agreed-upon terms. However, lenders will consider the business’s financial health and creditworthiness each time a new loan application is submitted.</p>
    
    <p><u><b>17. Is an SBA Express Loan a good option if my business is just starting out?</u></b><br>
    • Answer: While SBA Express Loans are primarily designed for businesses that are at least two years old, startups with a solid business plan, revenue projections, and personal creditworthiness may still be eligible. However, newer businesses may find it more challenging to meet the SBA’s criteria for a loan, and they might be better suited for other types of financing, like angel investing or venture capital.</p>             
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def smallbusinessadministrationexpresstwelve(request):
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
    Capital Type: SBA Express Loans</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    The ideal stage for using an SBA Express Loan is when the business is in its growth or mature stage, has a stable revenue stream, and needs short-term working capital or financing for specific business expansion needs. The loan is designed to be fast and flexible for businesses that meet these criteria.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    <br>LLCs and Corporations (especially S-Corps and C-Corps) are the most common and ideal entity types for SBA Express Loans, offering flexibility and structure while meeting the SBA’s requirements. Sole Proprietorship, Partnership and Cooperatives are less common but may still meet the requirements of the loan.
    <br>All of these entity types can apply for SBA 7(a) loans as long as the business is for-profit, small in size (according to SBA standards), and meets other SBA eligibility criteria. Generally, SBA 7(a) loans are accessible to a wide range of businesses, with entity type being just one of the considerations in the loan application process. 
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    Having raised pre-capital is not an obstacle to applying for an SBA Express loan as long as your business meets the SBA's criteria for eligibility, and the pre-capital does not cause issues with repayment capacity or the loan terms. In fact, it can demonstrate that your business is well-funded and has a viable plan for growth, which may strengthen your application. Just ensure that any prior investments or loans are documented properly and that your business can clearly show how it will use the SBA loan for its intended purposes.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    Raising pre-capital in any market is not inherently problematic for SBA Express loans but businesses must ensure that their capital structure is clear, compliant with SBA guidelines, and free from any conflicts that could hinder their ability to meet loan requirements or cause potential repayment issues. Proper documentation, transparency, and a clear plan for how the capital has been used are essential for a successful SBA loan application.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    The SBA Express loan can lend up to $500,000 for qualified businesses.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    The ideal capital round for a company seeking an SBA Express loan would generally be post-seed or early-stage funding, where the business has established itself with some revenue, possibly a growth phase with initial sales, and now needs capital for working capital, inventory, or equipment. A company in the growth stage (after Series A) or with previous debt financing would also be well-positioned for an SBA Express Loan, as long as it meets SBA requirements for financial health and repayment capacity.</p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    SBA Express Loans are designed to be single-disbursement loans. If you need ongoing access to capital or additional funds, you would have to apply for separate loans or explore different SBA loan products, such as a line of credit under the SBA 7(a) program.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    SBA Express loans offer great flexibility and can be used for a wide range of business purposes, including working capital, equipment purchases, expansion, acquiring real estate, refinancing debt, and even franchise fees. The goal is to help businesses manage and grow their operations, stabilize their finances, and position themselves for long-term success.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    A business seeking an SBA Express loan should ideally have a moderate risk tolerance. This is because SBA loans come with repayment commitments, collateral requirements (over $25,000), and the need to manage financial stability amid fluctuating cash flows, market conditions, and external risks. The business should have a proven ability to generate stable revenue, a reasonable growth outlook, and the capacity to repay the loan over time.
    <br>Businesses that are in the early stages of development or those operating in highly volatile sectors should carefully consider their financial capacity and the potential risks before applying for an SBA Express loan. 
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    When applying for an SBA Express loan, a business should have a low to moderate capital cost tolerance. The capital costs associated with an SBA Express loan include both upfront expenses (such as loan fees and closing costs) and ongoing costs related to interest and repayment. The repayment period is shorter for an Express loan than a standard 7(a) loan.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    For a loan under $150,000, the total upfront costs (including fees) could range from 2% to 5% of the loan amount. For larger loans, the costs could be higher, typically around 3% to 5% of the loan amount.
    <br>For example, if you take out an SBA Express Loan for $100,000, the upfront costs (including guarantee fees and any additional lender fees) might range from $2,000 to $5,000.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    An SBA Express Loan can be processed quickly, often within 36 hours from the time the application is submitted. The SBA Express loan program is designed to expedite the application and approval process compared to standard SBA loans. Since the loan limit for SBA Express loans is $500,000, this quicker turnaround is particularly useful for businesses that need immediate access to capital. However, the speed depends on how quickly you can provide the required documentation and how efficiently the lender processes it. It's important to note that the timeline can vary depending on the lender’s specific procedures and your business’s financial situation.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)