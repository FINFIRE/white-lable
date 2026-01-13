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


def smallbusinessadministration504B(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Small Business Administration</b></u><br>
    Capital Type: 504 Loans</center></p>
    
    <p><b><u>Introduction</u></b><br>
    In FY23, the SBA’s 504 program delivered more than 5,900 fixed-rate loans for equipment, real estate, and debt refinancing worth more than $6.4 billion to small businesses <a href="https://www.sba.gov/article/2023/11/21/sba-announces-biden-harris-administrations-progress-small-business-lending-end-year-capital-program">(source)</a>. In the first half of 2024 the SBA approved 3,306 504 loans for $3,619,017,000 <a href="https://www.federalregister.gov/documents/2024/10/01/2024-22040/504-debt-refinancing">(source)</a>.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    1) The 504 loan program provides long-term, fixed rate financing for major fixed assets that promote business growth and job creation. 504 loans are available through Certified Development Companies (CDCs), SBA's community-based nonprofit partners who promote economic development within their communities. CDCs are certified and regulated by SBA. The maximum loan amount for a 504 loan is $5.5 million. (504 Loans, 2024)

    <br><br>2) The CDC/504 loan program is a long-term financing tool, designed to encourage economic development within a community. A Certified Development Company (CDC) is a private, nonprofit corporation which is set up to contribute to economic development within its community. CDCs work with SBA and private sector lenders to provide financing to small businesses, which accomplishes the goal of community economic development. Typically, a CDC/504 project includes: 1) a loan secured from a private sector lender with a senior lien covering up to 50% of the project cost; 2) a loan secured from a CDC (backed by a 100% SBA-guaranteed debenture) with a junior lien covering up to 40% of the project cost; 3) a contribution from the borrower of at least 10% of the project cost (equity); and 4) this type of setup means that 100% of the project cost is covered either by contribution of equity by the borrower, or the senior or junior lien. Proceeds from 504 loans must be used for fixed asset projects, such as: 1) the purchase of land, including existing buildings; 2) the purchase of improvements, including grading, street improvements, utilities, parking lots and landscaping; 3) the construction of new facilities or modernizing, renovating or converting existing facilities; and 4) The purchase of long-term machinery and equipment.

    <br><br>To be eligible for a CDC/504 loan, the business must be operated for profit and fall within the size standards set by the SBA. Under the 504 Program, a business qualifies as small if it does not have a tangible net worth in excess of $7,500,000 and does not have an average net income in excess of $2,500,000 after taxes for the preceding two years. Loans cannot be made to businesses engaged in speculation or investment in rental real estate. The maximum SBA debenture is $1,500,000 when meeting the job creation criteria or a community development goal. Generally, the business must create or retain one job for every $65,000 provided by the SBA, except for small manufacturers which have a $100,000 job creation or retention goal. (Smith, 2021)

    <br><br>3) The U.S. Small Business Administration (SBA) backs the loans, but it does not provide the funds. CDCs, which are economic development nonprofits, work with banks and credit unions approved by the SBA to provide the funding. A CDC will provide 40% of the funding, while an SBA-approved bank or credit union will provide 50%. Borrowers are responsible for making a 10% contribution. (What Is the Required SBA 504 Loan Down Payment?, 2023) 
    </p>
                             
    <u><b><p>References</u></b><br>
    504 Loans. (2024, June 14). Retrieved from SBA: https://www.sba.gov/funding-programs/loans/504-loans
    <br><br>Smith, T. D. (2021). Business Capital 101. San Francisco: Imaginary Press.
    <br><br>What Is the Required SBA 504 Loan Down Payment? (2023, February 13). Retrieved from SBA 504: https://sba504.loans/sba-504-blog/what-is-the-required-sba-504-loan-down-payment/
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>• Operate as a for-profit company in the United States or its possessions
    <br>• Have an average net income of less than $5 million after federal income taxes for the two years preceding your application
    <br>• Your business must meet current SBA size standards.
    <br>• Your business’ net worth cannot exceed $15 million.
    <br>• Your business cannot earn 1/3 or more of its income from packaging SBA loans.
    <br>• Your business cannot be engaged in any sort of passive or speculative activities
    <br>• Good Character: Borrowers must pass a background check, and a criminal history—particularly financial-related offenses—may affect eligibility.
    <br>• Business Plan: A clear and feasible business plan is essential for showing how the loan will support business operations and growth.
    <br>• No Government Debt: Borrowers must not be delinquent on any federal loans, such as existing SBA loans or federal tax debts.
    <br>• The business must not have other available sources of funding
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• SBA Form 1244: This form verifies that the applicant is eligible for the SBA 504 loan program.
    <br>• SBA Form 912: Personal history statement, required for all owners with 20% or more ownership.
    <br>• Business Tax Returns: Typically, 3 years of business tax returns (e.g., Form 1040, 1065, or 1120).
    <br>• Financial Statements: At least 3 years of financial statements (balance sheet, income statement, and cash flow statement), ideally prepared by an accountant.
    <br>• Interim Financials: Year-to-date financial statements (monthly or quarterly).
    <br>• Debt Schedule: A list of all outstanding debts (business and personal, if applicable).
    <br>• Resume or Personal Background: A resume or business background summary for any key business owners or managers.
    <br>• Business Plan: A detailed business plan explaining the purpose of the loan, how funds will be used, and how the business intends to repay the loan.
    <br>• Articles of Incorporation: If applicable, the company's incorporation documents.
    <br>• Operating Agreement: For LLCs, an operating agreement outlining the management structure.
    <br>• Partnership Agreement: If applicable, a partnership agreement.
    <br>• Property Appraisal: A certified appraisal of the property or equipment being purchased or improved.
    <br>• Real Estate Documents: If the loan is for real estate, you may need to provide:
    <br>• Purchase agreement or lease agreement
    <br>• Deed of trust or mortgage
    <br>• Property tax statements
    <br>• Environmental Assessments: For certain properties, environmental assessments or reports (Phase I, for example) may be required.
    <br>• Franchise Agreement: If your business is a franchise, the franchise agreement may be required.
    <br>• Legal Structure Documentation: If there are changes to the business structure (e.g., mergers or acquisitions), related documents must be submitted.
    <br>• Business Licenses and Permits: Local, state, and federal licenses and permits, depending on the type of business.
    <br>• Cost Breakdown: Detailed estimates and cost breakdowns for the purchase or construction of the property or equipment being financed.
    <br>• Construction Contracts or Agreements: If the loan is for construction, signed contracts or agreements with contractors or vendors.
    <br>• Lease Agreements: If the loan is used for leasehold improvements, copies of lease agreements.
    </p>
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def smallbusinessadministration504Bfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Small Business Administration<br>
    Capital Type: 504 Loans</center></p>                        
    <p><center><u><b>Frequently Asked Question for 504 Loans</u></b></center></p>
    <p><u><b>1. What is an SBA 504 loan and how does it work?</u></b><br>
    • Answer: An SBA 504 loan is a government-backed loan designed to help small businesses purchase or improve fixed assets like real estate, buildings, or equipment. The loan is structured in two parts: a 50-90% portion funded by a Certified Development Company (CDC), and a 10-50% portion provided by a commercial lender. The business is required to provide at least 10% in equity as a down payment.</p>
                             
    <p><u><b>2. What types of projects can I use an SBA 504 loan for?</u></b><br>
    • Answer: SBA 504 loans are intended for long-term, fixed assets. Common uses include:
    <br>- Purchasing real estate (land or buildings)
    <br>- Renovating or constructing commercial properties
    <br>- Purchasing machinery, equipment, or large-scale assets that will help the business grow and increase productivity.</p>
                             
    <p><u><b>3. How is an SBA 504 loan different from other loan types, like SBA 7(a) or traditional bank loans?</u></b><br>
    • Answer: The key differences include:
    <br>- SBA 504 loans typically have lower interest rates and longer repayment terms (10, 20, or 25 years), making them ideal for large, capital-intensive projects.
    <br>- Unlike SBA 7(a) loans, which are more flexible for general working capital, SBA 504 loans are specifically for fixed assets and require a down payment of 10% to 20% of the project cost.
    <br>- Traditional bank loans often have higher interest rates and stricter terms, whereas SBA 504 loans offer fixed rates and are more accessible to small businesses with a lower down payment requirement.</p>
                             
    <p><u><b>4. Who qualifies for an SBA 504 loan?</u></b><br>
    • Answer: To qualify, businesses must meet the following criteria:
    <br>- Operate as a for-profit company in the U.S..
    <br>- Have a net worth under $15 million and average net income under $5 million over the last two years.
    <br>- Use the loan for eligible fixed asset purchases or improvements.
    <br>- The business should be able to demonstrate its ability to repay the loan and maintain an adequate cash flow.</p>
                             
    <p><u><b>5. How much can I borrow with an SBA 504 loan?</u></b><br>
    • Answer: The maximum SBA 504 loan amount is generally $5 million for most projects. For green or energy-efficient projects, the limit increases to $5.5 million. The SBA portion of the loan typically covers 50% to 90% of the project cost, depending on the risk level of the business and project.
    </p>
                             
    <p><u><b>6. What are the interest rates and repayment terms for an SBA 504 loan?</u></b><br>
    • Answer: Interest rates for SBA 504 loans are generally lower than traditional bank loans and are fixed for the life of the loan. Rates are based on the 5-year or 10-year U.S. Treasury bond rates, plus a margin set by the CDC and commercial lender. Repayment terms can range from 10 to 25 years, depending on the asset type and the term length chosen.</p>
                             
    <p><u><b>7. How long does it take to get an SBA 504 loan?</u></b><br>
    • Answer: On average, the process takes about 60 to 90 days from application to funding. The timeline can vary depending on the complexity of the project, the responsiveness of all parties, and the thoroughness of the documentation provided.</p>
                             
    <p><u><b>8. What are the upfront costs of an SBA 504 loan?</u></b><br>
    • Answer: Typical upfront costs include:
    <br>- Down payment (typically 10% to 20% of the total project cost)
    <br>- Closing costs, which can range from 2% to 5% of the loan amount
    <br>- Appraisal, environmental, and title fees, which can total $3,000 to $10,000+ depending on the project
    <br>- Legal and consultant fees may also apply.</p>
                             
    <p><u><b>9. What are the advantages of an SBA 504 loan compared to other types of financing?</u></b><br>
    • Answer:     
    <br>- Low, fixed interest rates: SBA 504 loans offer lower interest rates compared to conventional loans, with rates typically based on U.S. Treasury bond rates.
    <br>- Long repayment terms: SBA 504 loans offer terms of up to 25 years, allowing for lower monthly payments and improved cash flow management.
    <br>- Lower down payment requirements: SBA 504 loans generally require only a 10% equity contribution, which is much lower than traditional loans, making it easier for small businesses to access funding.
    <br>- No balloon payments: SBA 504 loans do not require balloon payments, which helps businesses avoid larger-than-expected lump sum payments.
    <br>- Ability to finance large, long-term assets: These loans are specifically designed for large capital expenditures, such as purchasing real estate or expensive equipment.</p>
                             
    <p><u><b>10. What are the risks or downsides of using an SBA 504 loan?</u></b><br>
    • Answer:     
    <br>- Restricted use: SBA 504 loans can only be used for purchasing or improving fixed assets. Businesses cannot use the funds for working capital, inventory, or other short-term expenses.
    <br>- Lengthy application process: The application process can be time-consuming, requiring significant documentation and third-party reports (e.g., appraisals, environmental assessments).
    <br>- Equity contribution: Businesses need to contribute 10% to 20% of the total project cost, which might be challenging for some businesses, particularly startups or businesses with limited capital.
    <br>- Collateral requirements: The assets being financed are often used as collateral, which means that if the business defaults, the lender can seize those assets.</p>
                             
    <p><u><b>11. Can I refinance an existing loan with an SBA 504 loan?</u></b><br>
    • Answer: Yes, SBA 504 loans can be used to refinance existing debt if the debt is tied to eligible fixed assets (e.g., real estate or equipment). Refinancing is subject to certain conditions, including 50% or more of the loan proceeds being used for eligible improvements or refinancing debt that is in place for at least two years.</p>
                             
    <p><u><b>12. Can I use an SBA 504 loan for a startup or new business?</u></b><br>
    • Answer: Yes, startups and new businesses can apply for SBA 504 loans, but they may face more stringent requirements. The down payment could be as high as 15-20%, and the business will need to demonstrate a strong business plan and the ability to repay the loan. Startups may also face additional challenges in terms of creditworthiness and collateral.
    </p> 
                             
    <p><u><b>13. How does an SBA 504 loan impact my business’s credit and financial standing?</u></b><br>
    • Answer: SBA 504 loans are reported to business credit bureaus and will impact the company’s credit standing, just like any other loan. Timely repayments will help build credit, while late or missed payments can harm the business's credit rating. Additionally, businesses may need to show a strong financial track record, especially in the case of startups or businesses with less than five years of operation.</p>

    <p><u><b>14. How does the SBA 504 loan affect my ability to raise capital in the future?</u></b><br>
    • Answer: Using an SBA 504 loan can demonstrate to other lenders or investors that the business is capable of securing favorable financing terms. However, since the SBA 504 loan is a secured loan, it could reduce the business’s ability to pledge assets for future borrowing. Additionally, the ongoing debt service may be a factor in future financing applications.</p>
    
     <p><u><b>15. What are the key eligibility requirements for an SBA 504 loan?</u></b><br>
    • Answer:     
    <br>- The business must be a for-profit business located in the U.S..
    <br>- Net worth should not exceed $15 million, and average net income should be below $5 million.
    <br>- The loan is for purchasing, constructing, or improving fixed assets (real estate, machinery, equipment).
    <br>- The business must demonstrate the ability to repay the loan and maintain positive cash flow.</p>             
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def smallbusinessadministration504Btwelve(request):
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
    Capital Type: SBA 504 Loans</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    The ideal candidate for an SBA 504 loan is an established small business with at least two years of operation, a track record of positive cash flow, a clear need for long-term capital to grow, and sufficient collateral to back the loan. This type of loan is not typically suited for startups, high-risk ventures, or businesses in early development stages that do not have solid financials and growth potential.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    While LLCs, corporations (C-Corp or S-Corp), and partnerships are the most common and ideal entities for securing an SBA 504 loan, other entity types such as sole proprietorships can also apply. However, the entity should be well-established with a proven track record of profitability and the capacity to meet the SBA's collateral, size, and operational criteria.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    Businesses are allowed to have raised pre-capital before applying for an SBA 504 loan, but the business must still meet all SBA eligibility requirements. The key considerations are ensuring the business is still small according to SBA standards, has clear ownership, and uses the funds appropriately for long-term growth (like purchasing real estate or equipment). In some cases, businesses with substantial external investment may need to provide additional documentation or clarification about their financial structure, but this will not disqualify them outright from receiving an SBA 504 loan.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    While it is generally acceptable for businesses to have raised pre-capital before applying for an SBA 504 loan, certain types of capital and ownership structures can interfere with the eligibility for an SBA 504 loan. Issues arise when investors have excessive control over the business, the company becomes over-leveraged with debt, or the raised capital creates conflicts with SBA’s guidelines for small business control and independence. It’s important for businesses to ensure that they remain within SBA’s requirements for size, ownership, and control, and to disclose all relevant information about their pre-capital when applying for the loan.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    The SBA 7504 loan program can lend up to $5.5 million for qualified businesses. </p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    For a business seeking an SBA 504 loan, the ideal capital round is usually post-seed or Series A, when the business has achieved some level of maturity (typically 2+ years in operation), has stabilized cash flow, and is ready to acquire assets such as real estate or equipment to support growth. The key factors are that the business must maintain control and ownership, demonstrate financial stability, and have a clear growth plan that aligns with the SBA 504 loan’s purpose.</p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    The SBA 504 loan typically does not allow for raising capital through multiple tranches in the way that private equity or venture capital rounds are structured. The SBA 504 loan is a government-backed loan program designed to help small businesses acquire long-term assets like real estate, equipment, or machinery. The loan is structured as a single, long-term financing package and is not typically used in multiple tranches or stages. If you need capital in stages for ongoing business needs, you may need to consider other financing options that provide more flexibility.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    The funds from an SBA 504 loan are meant to help businesses acquire and improve long-term fixed assets such as real estate, land, buildings, and equipment. These funds are intended to support business growth and expansion through investments that have a long-term, tangible impact on the business’s infrastructure. The loan cannot be used for working capital, inventory, or operational costs but is ideal for companies looking to invest in assets that will help them scale or improve efficiency over time.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    A business looking to use an SBA 504 loan needs to have a moderate risk tolerance, especially when it comes to financial stability, long-term commitments, and debt management. The ideal business would have stable cash flow, a clear growth plan, and long-term investment goals that align with purchasing or improving fixed assets like real estate or equipment. While the SBA 504 loan offers low interest rates and favorable terms, the company must be prepared for the risks associated with taking on long-term debt and committing to asset ownership in a changing business environment.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    Businesses applying for an SBA 504 loan should have a moderate to low tolerance for capital cost commitments because the loan is designed to cover large, long-term capital expenditures. Businesses need to have a solid financial foundation, adequate reserves, and a clear growth strategy to ensure they can comfortably manage the capital costs involved in using an SBA 504 loan.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    The upfront costs for a business applying for an SBA 504 loan typically consist of several components, including the down payment, closing costs, and sometimes fees associated with appraisals, environmental reports, and other services. These costs can vary depending on the size of the project, the lender, the specific circumstances of the business, and the type of property or asset being purchased. This amount can range between $125,000 to $170,000 for a $1,000,000 project, but the actual costs will depend on specific circumstances and requirements.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    The timeline for securing an SBA 504 loan can vary based on several factors, including the complexity of the project, the lender's processing times, the completeness of the application, and whether the business is fully prepared. On average, businesses can expect to receive an SBA 504 loan approval in about 60 to 90 days.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)