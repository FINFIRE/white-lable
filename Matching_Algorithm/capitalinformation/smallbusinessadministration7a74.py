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


def smallbusinessadministration7a(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Small Business Administration</b></u><br>
    Capital Type: 7(a) Loans</center></p>
    
    <p><b><u>Introduction</u></b><br>
    SBA 7(a) loans are ideal for small businesses seeking financing amounts up to $5 million in a 1–3-month period. These loans are designed to provide businesses with working capital, equipment financing, or funds for expansion, making them highly versatile. However, there are some risks like collateral, long application processes, and debt burden. For {n}, the SBA 7(a) loan program is a viable option for securing the necessary capital to grow operations. The program has been a critical tool for small businesses for decades, with over $24.2 billion in SBA 7(a) loans approved during the fiscal year 2024 alone. In 2023, SBA 7(a) loans supported thousands of businesses across various industries, with the average loan amount being approximately $420,000. This program continues to be a crucial funding resource for small to medium-sized enterprises, providing flexible terms, competitive interest rates, and government-backed guarantees to help businesses thrive.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br>1. An SBA 7(a) loan refers to a government-backed loan program provided by the U.S. Small Business Administration (SBA) to help small businesses secure financing for a variety of purposes, including working capital, equipment purchases, debt refinancing, and business expansion. The SBA guarantees a portion of the loan, reducing the risk for lenders and making it easier for small businesses to obtain funding. SBA 7(a) loans offer flexible terms, competitive interest rates, and loan amounts up to $5 million, making them a popular option for businesses seeking long-term financing. (SBA, 2024)
<br>
    <br>2. The 7(a) Loan Program, SBA’s primary business loan program, provides loan guaranties to lenders that allow them to provide financial help for small businesses with special requirements. 7(a) loans can be used for: 
    <br>• Acquiring, refinancing, or improving real estate and buildings
    <br>• Short- and long-term working capital 
    <br>• Refinancing current business debt 
    <br>• Purchasing and installation of machinery and equipment, including AI-related expenses
    <br>• Purchasing furniture, fixtures, and supplies 
    <br>• Changes of ownership (complete or partial)
    <br>• Multiple purpose loans, including any of the above 
    <br>(7(a) Loans, 2024)
<br>
    <br>3. The SBA 7(a) loan program provides small businesses with loans of up to $5 million. The exact loan amount that a business can receive is determined by factors such as the business’s financial needs, its ability to repay the loan, and the specific purpose of the loan. Common uses include working capital, purchasing equipment, real estate acquisition, and refinancing existing debt. The SBA guarantees up to 85% of loans up to $150,000 and up to 75% of loans greater than $150,000, making it easier for small businesses to secure the necessary funding while reducing the lender’s risk. (SBA, 2024)
<br>
    <br>4. While SBA 7(a) loans offer many benefits, they also come with certain risks. One major risk is the requirement for a personal guarantee from business owners, meaning that if the business fails to repay the loan, the owners' personal assets, such as their home, could be at risk. Additionally, these loans may require collateral, and the business could lose valuable assets if it defaults on the loan. The application process for an SBA 7(a) loan can also be time-consuming and complex, requiring extensive documentation and approval from both the lender and the SBA. Furthermore, if the business struggles with cash flow or financial instability, it may have difficulty making the loan repayments, potentially harming its credit and increasing financial strain. Lastly, while the SBA 7(a) loan offers flexible terms, interest rates can be higher than other forms of financing, depending on the lender and the business’s creditworthiness, which can lead to increased long-term costs. (SBA, 2024)
<br>
    <br>5. The timeframe for obtaining an SBA 7(a) loan typically ranges from a few weeks to a few months, depending on various factors such as the complexity of the loan, the lender’s processing speed, and the completeness of the application. The application process involves gathering and submitting detailed financial documentation, including tax returns, business plans, and financial statements. Once the lender receives the application, it usually takes 2 to 4 weeks for initial approval. Afterward, the SBA’s review and guarantee process may take additional time, potentially extending the overall timeline to 30 to 90 days. However, if the business has a strong financial history and the application is straightforward, the approval process may be faster. Additionally, SBA 7(a) loans can have a repayment term of up to 25 years, depending on the loan’s purpose (e.g., real estate loans can have longer terms than working capital loans). (SBA, 2024)
    </p>
                             
    <u><b><p>References</u></b><br>
    <br>U.S. Small Business Administration. (2024). 7(a) Loan Program. Retrieved from <a href="https://www.sba.gov/funding-programs/loans/7a-loans">https://www.sba.gov/funding-programs/loans/7a-loans</a>
<br>
    <br>SBA 7(A) Loans. (2024, March 25). FEMA.gov. <a href="https://www.fema.gov/emergency-managers/practitioners/recovery-resilience-resource-library/sba-7a-loans">https://www.fema.gov/emergency-managers/practitioners/recovery-resilience-resource-library/sba-7a-loans</a>
<br>
    <br>7(a) Loans. (2024, July 24). Retrieved from SBA: <a href="https://www.sba.gov/funding-programs/loans/7a-loans">https://www.sba.gov/funding-programs/loans/7a-loans</a>
<br>
    <br>SBA 7(A) and SBA 504 loans for business financing | Wells Fargo. (n.d.). <a href="https://www.wellsfargo.com/biz/sba/">https://www.wellsfargo.com/biz/sba/</a>
<br>
    <br>Bankers’ Guide to the SBA 7(a) Loan Guaranty. (n.d.). Retrieved from OCC: <a href="https://www.occ.gov/publications-and-resources/publications/community-affairs/community-developments-insights/pub-insights-dec-2014.pdf">https://www.occ.gov/publications-and-resources/publications/community-affairs/community-developments-insights/pub-insights-dec-2014.pdf</a>
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br><br>1. Business Structure: The business must be a for-profit entity and legally registered in the U.S. as a sole proprietorship, partnership, LLC, or corporation. It must be an active business operating in the United States or its territories.
    <br><br>2. U.S. Citizenship or Legal Residency: The owners of the business must be U.S. citizens or legal permanent residents. Non-U.S. citizens may be eligible if they meet specific requirements, such as having legal residency status.
    <br><br>3. Eligible Industry: The business must not be involved in activities deemed ineligible by the SBA, such as illegal activities, gambling, speculative real estate, or lending businesses. Certain types of passive real estate investment are also ineligible.
    <br><br>4. Size Standards: The business must qualify as a small business according to SBA size standards, which depend on industry and are typically based on the business’s average annual revenue or number of employees.
    <br><br>5. Repayment Ability: The business must be able to demonstrate its ability to repay the loan. Lenders assess repayment capacity by reviewing financial statements, tax returns, business performance, and projected cash flow.
    <br><br>6. Good Character: The business owners must have a clean criminal record, with no felony convictions involving dishonesty or breach of trust. Lenders will also evaluate the personal credit history of the owners.
    <br><br>7. Equity Investment: The business owners must have a reasonable level of equity investment in the business. This shows a commitment to the business’s success and ensures the owners are financially at risk.
    <br><br>8. Use of Funds: The business must use the loan for eligible business purposes, such as working capital, purchasing equipment or real estate, or refinancing existing debt.
    <br><br>9. No Delinquent Federal Debts: The business or its owners must not have any outstanding or delinquent federal debt, such as unpaid taxes or government loans.
    <br><br>10. Ability to Operate: The business must be able to demonstrate that it is capable of operating and will continue to do so after receiving the loan, showing that it is viable and stable.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Loan Application (SBA Form 1919): Basic information about the business and loan request.
    <br>• Personal Background and Financial Statement (SBA Form 413): Financial details of business owners with 20%+ stake.
    <br>• Business Financial Statements: Balance sheets, profit & loss statements, cash flow statements, and business tax returns for the last 3 years.
    <br>• Business Plan: Outlines business goals, loan use, and financial projections.
    <br>• Ownership and Affiliations: Information on business ownership structure and affiliated businesses.
    <br>• Lease or Property Deed: Lease agreement or property deed if the loan involves real estate.
    <br>• Collateral: Description and valuation of assets used as collateral.
    <br>• Legal Documents: Articles of incorporation, partnership agreements, business licenses, and other legal documents.
    <br>• Debt Schedule: A list of current business debts if refinancing is involved.
    <br>• Other Documents: Resumes for key management, franchise agreements (if applicable), and personal tax returns for the last 3 years.
    </p>
        """)
    name = name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def smallbusinessadministration7afaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Small Business Administration<br>
    Capital Type: 7(a) Loan</center></p>                        
    <p><center><u><b>Frequently Asked Question for 7(a) Loan</u></b></center></p>
    <p><u><b>1. What is an SBA 7(a) loan?</u></b><br>
    • Answer: The SBA 7(a) loan program is a government-backed loan designed to help small businesses obtain financing for various purposes, including working capital, equipment, real estate, or refinancing existing debt. It is one of the most common and flexible SBA loan programs.</p>
                             
    <p><u><b>2. Why should my business choose an SBA 7(a) loan over other financing options?</u></b><br>
    • Answer: SBA 7(a) loans often offer lower interest rates and longer repayment terms than conventional loans, making them an attractive choice for businesses seeking affordable capital. Additionally, the SBA guarantee reduces lender risk, making it easier for small businesses to qualify.</p>
                             
    <p><u><b>3. How much can I borrow with an SBA 7(a) loan?</u></b><br>
    • Answer: The maximum loan amount for an SBA 7(a) loan is $5 million. However, the loan amount your business qualifies for will depend on factors like your business's financial health, creditworthiness, and ability to repay the loan.</p>
                             
    <p><u><b>4. What are the interest rates for SBA 7(a) loans?</u></b><br>
    • Answer: Interest rates for SBA 7(a) loans are typically lower than those of traditional bank loans. Rates vary based on the loan amount and the repayment term, but they are generally tied to the prime rate with a margin added. Rates range from 7% to 9% for most loans, but they are subject to SBA guidelines.</p>
                             
    <p><u><b>5. What can I use an SBA 7(a) loan for?</u></b><br>
    • Answer: SBA 7(a) loans can be used for a variety of business purposes, including:
    <br>- Working capital
    <br>- Equipment purchases
    <br>- Buying or refinancing real estate
    <br>- Business acquisition
    <br>- Franchise financing
    <br>- Debt refinancing
    <br>- Expansion and improvement costs
    </p>
                             
    <p><u><b>6. What are the eligibility requirements for an SBA 7(a) loan?</u></b><br>
    • Answer: To qualify for an SBA 7(a) loan, your business must meet certain criteria, including:
    <br>- Be a for-profit business operating in the U.S.
    <br>- Meet the SBA's definition of a small business.
    <br>- Have a sound business plan.
    <br>- Show the ability to repay the loan.
    <br>- Demonstrate good character, credit, and a solid track record of business operations.
    <br>- The business owner must have invested equity in the business.</p>
                             
    <p><u><b>7. What are the repayment terms for an SBA 7(a) loan?</u></b><br>
    • Answer: SBA 7(a) loans offer flexible repayment terms depending on the loan purpose. For example:
    <br>- Working capital or short-term financing: Up to 7 years.
    <br>- Equipment or real estate financing: Up to 10 years or 25 years (for real estate).
    <br>- Repayment terms are often longer than conventional loans, making monthly payments more manageable.</p>
                             
    <p><u><b>8. What collateral is required for an SBA 7(a) loan?</u></b><br>
    • Answer: SBA 7(a) loans may require collateral, depending on the size and purpose of the loan. Common collateral includes real estate, equipment, and business assets. However, the SBA does not require full collateral for loans under $25,000, and lenders are encouraged to be flexible.</p>
                             
    <p><u><b>9. Are there any fees associated with SBA 7(a) loans?</u></b><br>
    • Answer: Yes, SBA 7(a) loans come with various fees, including:
    <br>- A guarantee fee, which depends on the loan size.
    <br>- Application and processing fees from the lender.
    <br>- Closing costs and other administrative charges.
    <br>- These fees are typically lower than the fees associated with traditional loans, but they should still be considered when evaluating the overall cost.</p>
                             
    <p><u><b>10. How long does it take to get approved for an SBA 7(a) loan?</u></b><br>
    • Answer: The approval process for SBA 7(a) loans can take anywhere from a few weeks to a few months, depending on the complexity of the application, the lender’s process, and the business’s financial standing. The SBA generally takes about 5-10 business days to review the application after it is submitted.</p>
                             
    <p><u><b>11. How does an SBA 7(a) loan compare to other government-backed loans?</u></b><br>
    • Answer: The SBA 7(a) loan is the most versatile of the SBA loan programs, compared to options like the SBA CDC/504 loan, which is specifically designed for real estate and large equipment purchases. The 7(a) loan is better suited for businesses needing working capital or multiple types of funding, while the CDC/504 loan offers lower interest rates for fixed asset purchases.</p>
                             
    <p><u><b>12. What if my business doesn’t qualify for an SBA 7(a) loan?</u></b><br>
    • Answer: If you don't qualify for an SBA 7(a) loan, there may be alternative financing options available, such as traditional bank loans, lines of credit, or loans from online lenders. It's important to review the specific requirements of each option to find the best fit for your business’s needs.
    </p> 
                             
    <p><u><b>13. Can I use an SBA 7(a) loan to refinance existing debt?</u></b><br>
    • Answer: Yes, SBA 7(a) loans can be used to refinance existing debt if the debt is considered high-interest or burdensome. This can help reduce monthly payments or provide more favorable terms.</p>

    <p><u><b>14. Are there restrictions on how I can spend the loan proceeds?</u></b><br>
    • Answer: While the SBA 7(a) loan is highly flexible, the loan proceeds must be used for eligible business purposes, such as working capital, equipment, or real estate. Using the funds for personal expenses, or other ineligible purposes, can lead to default and repayment issues.</p>
    
     <p><u><b>15. How does the SBA 7(a) loan affect my personal credit and business credit?</u></b><br>
    • Answer: Since the SBA guarantees part of the loan, the lender will still look at both your personal and business credit scores when assessing your application. A personal guarantee from the business owner is often required, meaning any issues with repayment could impact both personal and business credit scores.</p>
    
    <p><u><b>16. What happens if my business can’t repay the SBA 7(a) loan?</u></b><br>
    • Answer: If your business fails to repay the loan, the lender may take legal action to recover the funds. The SBA guarantee helps reduce the lender's risk, but they may still pursue repayment through business or personal assets, depending on the loan’s structure and the guarantee.</p>
    
    <p><u><b>17. Can I apply for an SBA 7(a) loan if I already have other loans?</u></b><br>
    • Answer: Yes, you can apply for an SBA 7(a) loan even if you have other outstanding loans. However, your ability to repay existing debts will be factored into the loan evaluation. The SBA 7(a) loan can be used to consolidate or refinance existing debt in certain cases.</p>             
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def smallbusinessadministration7atwelve(request):
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
    Capital Type: SBA 7(a) Loans</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    The growth or expansion stage is the ideal development stage for an SBA 7(a) loan. It is particularly suited for businesses that are established, with a track record of operations and revenue generation, looking to scale their operations, make capital investments, or refinance debt. These businesses typically benefit from the SBA’s favorable loan terms and guarantees, which make financing more accessible than through traditional bank loans.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    The ideal entity types for applying for an SBA 7(a) loan are:
    <br>• LLCs (Limited Liability Companies) – Ideal for their flexibility and liability protection.
    <br>• Corporations (C-Corps and S-Corps) – Good for businesses with formalized structures, especially those looking for growth.
    <br>• Partnerships – Suitable for smaller businesses that want to share responsibility and liability.
    <br>• Sole Proprietorships – For individual business owners with solid personal credit and a strong financial track record.

    <br><br>All of these entity types can apply for SBA 7(a) loans as long as the business is for-profit, small in size (according to SBA standards), and meets other SBA eligibility criteria. Generally, SBA 7(a) loans are accessible to a wide range of businesses, with entity type being just one of the considerations in the loan application process. 
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    Having raised pre-capital is not an obstacle to applying for an SBA 7(a) loan as long as your business meets the SBA's criteria for eligibility, and the pre-capital does not cause issues with repayment capacity or the loan terms. In fact, it can demonstrate that your business is well-funded and has a viable plan for growth, which may strengthen your application. Just ensure that any prior investments or loans are documented properly and that your business can clearly show how it will use the SBA loan for its intended purposes.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    Raising pre-capital in any market is not inherently problematic for SBA 7(a) loans but businesses must ensure that their capital structure is clear, compliant with SBA guidelines, and free from any conflicts that could hinder their ability to meet loan requirements or cause potential repayment issues. Proper documentation, transparency, and a clear plan for how the capital has been used are essential for a successful SBA loan application.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    The SBA 7(a) loan program can lend up to $5 million for qualified businesses.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Series B and later-stage capital rounds, as well as bootstrapped businesses, are generally the ideal stages for applying for an SBA 7(a) loan, as they have the financial stability, business track record, and growth plans needed to meet the SBA’s eligibility criteria.</p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    It is possible to raise capital through multiple tranches with an SBA 7(a) loan, but the loan structure and disbursement schedule need to be carefully planned and approved by both the lender and the SBA. Each tranche must align with the SBA’s guidelines for permissible loan uses, and proper documentation and tracking are required. Eligibility criteria, repayment capacity, and specific use cases must be clearly demonstrated for each tranche of the loan.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    SBA 7(a) loans offer great flexibility and can be used for a wide range of business purposes, including working capital, equipment purchases, expansion, acquiring real estate, refinancing debt, and even franchise fees. The goal is to help businesses manage and grow their operations, stabilize their finances, and position themselves for long-term success.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    A business seeking an SBA 7(a) loan should ideally have a moderate risk tolerance. This is because SBA loans come with long-term repayment commitments, collateral requirements, and the need to manage financial stability amid fluctuating cash flows, market conditions, and external risks. The business should have a proven ability to generate stable revenue, a reasonable growth outlook, and the capacity to repay the loan over time.
    <br>Businesses that are in the early stages of development or those operating in highly volatile sectors should carefully consider their financial capacity and the potential risks before applying for an SBA 7(a) loan. Conversely, more established businesses with stable operations and solid financial projections are generally better positioned to handle the responsibility of taking on SBA debt.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    When applying for an SBA 7(a) loan, a business should have a moderate capital cost tolerance, as the loan involves borrowing a significant amount of money that must be repaid with interest over time. The capital costs associated with an SBA 7(a) loan include both upfront expenses (such as loan fees and closing costs) and ongoing costs related to interest and repayment.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    When budgeting for an SBA 7(a) loan, a business should account for several costs, both upfront and ongoing. The total amount to budget will depend on the loan size, purpose, and associated fees, as well as the structure of the repayment terms. 
    <br>The average upfront cost for an SBA 7(a) loan, primarily consisting of the SBA guarantee fee, typically ranges between 1% to 3.5% of the total loan amount depending on the loan size and borrower's credit profile, with larger loans generally having a slightly higher fee percentage; this means for a $500,000 loan, the upfront cost could be between $5,000 and $17,500.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    Businesses should expect to wait 4 to 8 weeks from the application submission to funding for an SBA 7(a) loan. However, the process can be shorter or longer depending on the business’s preparedness, the complexity of the loan, and the efficiency of the lender and SBA. Starting the process early and ensuring all required documents are in order can help minimize delays.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)