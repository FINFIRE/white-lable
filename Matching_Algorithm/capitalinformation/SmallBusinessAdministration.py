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


def SmallBusinessAdministration(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><b><u>Definition of Capital Market: Small Business Administration (SBA)</b></u><br></p>
    
    <p><b><u>Introduction</u></b><br>
    SBA financing is ideal for companies raising debt capital in amounts ranging from $50,000 to $5 million in a given 12-month period of time. It is designed so that the borrower may access capital through government-guaranteed loans distributed by approved lenders. <b>{n}</b> fits that definition. SBA financing has been a viable tool for small businesses for over 70 years. For example, in the first three quarters of FY 2023, over $20.6 billion was disbursed through the SBA’s 7(a) loan program alone. In total for FY 2023, the SBA approved 57,300 7(a) loans totaling $27.5 billion, and 5,000 504 loans totaling $5.8 billion. The Microloan program also issued over $100 million in smaller loans to startups and underserved businesses. On average, each SBA 7(a) loan approved in 2023 was approximately $480,000.  There are six types of Small Business Administration that we can match you with: 1) SBA 404B 2) SBA 7A, 3) SBA Express, 4) SBA Veteran, 5) SBA - CDC/SBDC, 6) SBA - SBIC. We will select the most appropriate type of SMall Business Administration loan as per your business need.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br>1. SBA financing refers to loan programs offered through the U.S. Small Business Administration (SBA) that provide small businesses with access to affordable, government-backed funding. Rather than lending money directly, the SBA partners with approved banks, credit unions, and other lenders by guaranteeing a portion of the loan—typically 50% to 90%—to reduce the lender’s risk. This makes it easier for small businesses to qualify for capital, even if they lack strong collateral or credit history. SBA financing includes several loan types, such as the popular 7(a) Loan Program for general business needs, the 504 Loan Program for long-term assets like real estate and equipment, and the Microloan Program for smaller loan amounts up to $50,000. These loans often feature favorable terms, such as low interest rates, longer repayment periods, and flexible use of funds. (SBA, n.d.)
<br>
    <br>2. The U.S. Small Business Administration (SBA) offers several financing options to help small businesses grow, each tailored to specific needs. The most common is the SBA 7(a) Loan, which provides up to $5 million for working capital, equipment, inventory, or real estate and is ideal for general business purposes. The SBA 504 Loan is designed for purchasing fixed assets like buildings or large equipment, offering long-term, fixed-rate financing through Certified Development Companies (CDCs). For very small businesses or startups, the SBA Microloan Program provides up to $50,000, typically used for inventory, supplies, or equipment. Additionally, the SBA CAPLines program offers revolving lines of credit to help manage short-term working capital needs, and the Export Loan Programs assist small businesses expanding into international markets. Each type of SBA financing has unique eligibility requirements and terms, offering flexible and affordable solutions based on the borrower’s stage and objectives. (Terms, conditions, and eligibility, n.d.)
<br>
    <br>3. The Small Business Administration (SBA) was established in 1953 through the Small Business Act, signed into law by President Dwight D. Eisenhower, to support and protect the interests of small businesses in the United States. One of its core missions became offering financial assistance through government-backed loan programs to businesses that may not qualify for traditional financing. Over the decades, SBA loan programs have evolved significantly. The flagship 7(a) Loan Program was introduced early on and remains the most widely used option for general business financing. In 1986, the SBA launched the 504 Loan Program to specifically support long-term, fixed asset financing for job creation and economic development. The Microloan Program was added in 1992 to serve very small businesses and startups needing loans under $50,000. SBA loan programs have also adapted to economic challenges—for example, the agency played a key role in stabilizing small businesses during the COVID-19 pandemic through programs like the Paycheck Protection Program (PPP) and Economic Injury Disaster Loans (EIDL). Today, SBA loans continue to serve as a vital lifeline for small businesses seeking capital with flexible terms and government-backed guarantees. (Congress, n.d.)
<br>
    <br>4. While SBA financing offers attractive terms and government backing, it also comes with several risks that companies should consider. First, the application process can be lengthy and complex, often requiring extensive documentation and financial disclosures, which may be burdensome for small teams. SBA loans also typically require personal guarantees from business owners, putting personal assets such as homes or savings at risk in the event of default. Additionally, SBA loans may come with restrictive covenants, including limits on how funds can be used or requirements to maintain certain financial ratios. For companies in rapid-growth or high-risk industries, these restrictions can limit operational flexibility. Lastly, even though interest rates are generally favorable, failing to meet payment obligations can damage both the business and the owner’s personal credit, potentially restricting future access to capital. (Lyons, 2025)
<br>
    <br>5. To raise capital via SBA financing, a company must meet several requirements. The business must be a for-profit entity operating in the United States and meet size standards defined by the SBA, which typically include limits on annual revenue and number of employees, depending on the industry. The company must also demonstrate a need for funding and show the ability to repay the loan. It should have a strong business plan and a track record of sound financial management. Additionally, the business must have sufficient collateral to secure the loan, and owners may be required to provide personal guarantees. The company must have good credit and, depending on the loan type, may need to be in operation for at least two years. Other key requirements include having a legal structure such as a corporation, LLC, or partnership, and ensuring the business has no outstanding federal tax liens or delinquencies. Finally, businesses in certain industries, such as gambling or speculation, are ineligible for SBA financing. (Loans, n.d.)
    </p>
                             
    <p><b><u>References</u></b><br>
    <br>Loans. (n.d.). U.S. Small Business Administration. <a href="https://www.sba.gov/funding-programs/loans?">https://www.sba.gov/funding-programs/loans?</a>
    <br>Terms, conditions, and eligibility. (n.d.). U.S. Small Business Administration. <a href="https://www.sba.gov/partners/lenders/7a-loan-program/terms-conditions-eligibility?">https://www.sba.gov/partners/lenders/7a-loan-program/terms-conditions-eligibility?</a>
    <br>Small Business Administration 7(A) Loan Guaranty Program. (n.d.). Congress.gov | Library of Congress. <a href="https://www.congress.gov/crs-product/R41146">https://www.congress.gov/crs-product/R41146</a>
    <br>Lyons, D. (2025, March 7). What rising SBA loan defaults mean for small businesses in 2025 — Rapid Business Plans. Rapid Business Plans. <a href="https://rapidbusinessplans.com/blog/2025/3/7/what-rising-sba-loan-defaults-mean-for-small-businesses-in-2025?">https://rapidbusinessplans.com/blog/2025/3/7/what-rising-sba-loan-defaults-mean-for-small-businesses-in-2025?</a>
    <br>Loans. (n.d.). U.S. Small Business Administration. <a href="https://www.sba.gov/funding-programs/loans?">https://www.sba.gov/funding-programs/loans?</a>
    </p>
                             
    <p><b><u>Qualification Requirements</u></b>
    <br>• Business Type: Must be a for-profit U.S. business.
    <br>• Size Standards: Must meet SBA’s size criteria based on industry metrics.
    <br>• Legal Status: Must be a registered entity (LLC, corporation, sole proprietorship).
    <br>• Good Standing: Must be in good standing with tax and regulatory agencies.
    <br>• Ownership: At least 51% ownership by U.S. citizens or legal residents.
    <br>• Eligible Industries: Certain industries like gambling and illegal activities are ineligible.
    <br>• Use of Funds: Funds must be for legal business purposes like working capital or equipment. 
    <br>• Repayment Ability: Must demonstrate the ability to repay through financial records.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Business Plan: A detailed plan outlining the company’s goals, operations, and how funds will be used.
    <br>• Financial Statements: Income statement, balance sheet, and cash flow statement, typically for the past 3 years.
    <br>• Tax Returns: Personal and business tax returns for the past 3 years.
    <br>• Ownership and Affiliations: Personal background and financial information for any individuals with 20% or more ownership.
    <br>• Legal Documents: Articles of incorporation, business licenses, operating agreements, and any partnership agreements.
    <br>• Debt Schedule: A list of any existing debts or liabilities the business has.
    <br>• Collateral: Documentation of assets available for collateral, such as property, equipment, or inventory.
    <br>• Personal Financial Statements: For business owners with significant equity, a personal financial statement may be required.
    <br>• Business Credit Report: The company’s credit history and ratings, which SBA lenders will review.
    <br>• Cash Flow Projections: A forecast of future business revenues and expenses, showing how the loan will be repaid.
    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def SmallBusinessAdministrationfaq(request):
    introduction = mark_safe("""
    <p><b><u>FAQs</u></b></p>                        
                             
    <p><b><u>1. What is SBA financing?</u></b><br>
    • Answer: SBA financing refers to loans and financial assistance programs provided by the U.S. Small Business Administration (SBA) to help small businesses obtain funding with favorable terms. These loans are backed by the SBA, which reduces the risk for lenders, making it easier for small businesses to qualify.
    </p>
                             
    <p><b><u>2. What types of SBA loans are available?</u></b><br>
    • Answer: The main types of SBA loans are:
    <br>- SBA 7(a) Loan: General-purpose loans for working capital, equipment, real estate, and more.
    <br>- SBA 504 Loan: Used for purchasing real estate and major equipment.
    <br>- SBA Microloan: Smaller loans (up to $50,000) for working capital and small business needs.
    <br>- SBA Express Loan: A faster SBA 7(a) loan option with quicker processing times.
    <br>- SBA Disaster Loans: For businesses affected by natural disasters.
    </p>
                             
    <p><b><u>3. Who is eligible for SBA loans?</u></b><br>
    • Answer: Eligibility varies by loan type, but in general, businesses must:
    <br>- Be a small business as defined by the SBA.
    <br>- Be a for-profit entity.
    <br>- Operate in the U.S. or its territories.
    <br>- Have a good credit score (typically above 650).
    <br>- Demonstrate the ability to repay the loan.
    <br>- Be able to provide collateral for the loan.
    </p>
                             
    <p><b><u>4. How much can I borrow with an SBA loan?</u></b><br>
    • Answer: Loan amounts vary by the type of loan:
    <br>- SBA 7(a) loans: Up to $5 million.
    <br>- SBA 504 loans: Up to $5 million for standard projects.
    <br>- SBA Microloans: Up to $50,000.
    <br>- SBA Express loans: Up to $500,000.
    </p>
                             
    <p><b><u>5. What are the interest rates for SBA loans?</u></b><br>
    • Answer: Interest rates depend on the loan type and the lender. Generally:
    <br>- SBA 7(a) loans: Rates can be variable or fixed, and the maximum rate is determined by the SBA, typically ranging from 5% to 10%.
    <br>- SBA 504 loans: Fixed rates that are lower than those for conventional loans.
    <br>- SBA Microloans: Typically have rates ranging from 7% to 13%.
    </p>
                             
    <p><b><u>6. How long does it take to get approved for an SBA loan?</u></b><br>
    • Answer: The approval process can take anywhere from 30 to 90 days, depending on the type of SBA loan and the complexity of the application. The time frame is longer for more complex loan programs.
    </p>
                             
    <p><b><u>7. What are the requirements for collateral?</u></b><br>
    • Answer: Collateral is generally required for SBA loans, but the SBA allows lenders to be more flexible with the collateral requirements than traditional lenders. It can include real estate, equipment, inventory, or personal assets.
    </p>
                             
    <p><b><u>8. Are SBA loans easy to get?</u></b><br>
    • Answer: While SBA loans generally have lower interest rates and longer repayment terms than traditional loans, they can be difficult to obtain due to the thorough application process. Lenders will require detailed financial statements, a solid business plan, and a good credit history.
    </p>
                             
    <p><b><u>9. Do SBA loans require a personal guarantee?</u></b><br>
    • Answer: Yes, SBA loans typically require a personal guarantee from business owners who have a 20% or greater ownership stake in the business. This means that owners are personally responsible for repaying the loan if the business defaults.</p>
                             
    <p><b><u>10. Can I use SBA loans for working capital?</u></b><br>
    • Answer: Yes, SBA 7(a) loans are ideal for working capital, which can be used for operating expenses such as payroll, inventory, and accounts payable.
    </p>

    <p><b><u>11. Can I apply for an SBA loan if I have bad credit?</u></b><br>
    • Answer: It is more challenging to qualify for an SBA loan with bad credit, but it is not impossible. The SBA does consider credit scores as part of the application process, and a higher credit score will improve your chances of approval. However, lenders may also consider other factors, such as the overall financial health of your business.</p>

    <p><b><u>12. What happens if I can’t repay my SBA loan?</u></b><br>
    • Answer: If your business is unable to repay its SBA loan, the lender may seek to recover the loan through collateral or other assets. The SBA may also step in to help resolve the situation, but you may be personally liable for repayment if you signed a personal guarantee. It is important to communicate with your lender if you anticipate repayment difficulties.</p>                                            
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def SmallBusinessAdministrationtwelve(request):
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
    
    #Up front Cost options
    up_front_cost_options ={
        'Minimum $0 - Maximum $499' : 'Doing SBA below $500 would not be possible and it is better if you find the required funds as SBA financing can be a cost-effective option compared to equity raises or traditional commercial loans—especially with lower interest rates and longer repayment terms.',
        'Minimum $500 - Maximum $999' : 'SBA financing can be a cost-effective option compared to equity raises or traditional commercial loans—especially with lower interest rates and longer repayment terms.',
        'Minimum $1000 - Maximum $2499' : 'SBA financing can be a cost-effective option compared to equity raises or traditional commercial loans—especially with lower interest rates and longer repayment terms.',
        'Minimum $2500 - Maximum $4999' : 'SBA financing can be a cost-effective option compared to equity raises or traditional commercial loans—especially with lower interest rates and longer repayment terms.',
        'Minimum $5000 - Maximum $9999' : 'SBA financing can be a cost-effective option compared to equity raises or traditional commercial loans—especially with lower interest rates and longer repayment terms.',
        'Minimum $10000 - Maximum $24999' : 'SBA financing can be a cost-effective option compared to equity raises or traditional commercial loans—especially with lower interest rates and longer repayment terms.',
        'Minimum $25000 - Maximum $49999' : 'SBA financing can be a cost-effective option compared to equity raises or traditional commercial loans—especially with lower interest rates and longer repayment terms.',
        'More than $50000+' : 'SBA financing can be a cost-effective option compared to equity raises or traditional commercial loans—especially with lower interest rates and longer repayment terms.',             
    }
    costanalysis = up_front_cost_options[upfrontcost]

    #Up front Cost options
    up_front_time_options ={
        '1 Day to 1 Week' : '1 day to 1 week would not be sufficient as the complexity of the loan and the lender’s review process requires more time for SBA loans.',
        '1 Week to 2 Week' : '1 week to 2 week would not be sufficient as the complexity of the loan and the lender’s review process requires more time for SBA loans.',
        '2 Weeks to 4 Weeks' : '2 week to 4 week would not be sufficient as the complexity of the loan and the lender’s review process requires more time for SBA loans.',
        '1 Month to 2 Months' : '1 month to 2 months would generally be sufficient to adress the complexity of the loan and the lender’s review process required for SBA loans.',
        '2 Months to 3 Months' : '2 months to 3 months would be sufficient to adress the complexity of the loan and the lender’s review process required for SBA loans.',
        '3 Months to 6 Months' : '3 month to 6 months would be sufficient to adress the complexity of the loan and the lender’s review process required for SBA loans.',
        '6 Months to 12 Months' : '6 month to 12 months would be sufficient to adress the complexity of the loan and the lender’s review process required for SBA loans.',
        'More than 1 year' : 'More than 12 months would be sufficient to adress the complexity of the loan and the lender’s review process required for SBA loans.',             
    }
    timeanalysis = up_front_time_options[upfronttime]

    premarketStr = ''
    for num,item in enumerate(premarket):
        if num == 0:
            premarketStr = premarketStr + str(item).lower()
        elif num == (len(premarket)-1):
                premarketStr = premarketStr +', and ' + str(item).lower()
        else:        
            premarketStr = premarketStr +', ' + str(item).lower()

    introduction = """
    <p><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Small Business Administration</p>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    As <b>{n}</b> advances into a <b>{stage}</b> stage, SBA-backed financing offers an accessible, lower-risk way to raise capital—particularly through structured debt like the SBA 7(a) or SBA 504 loan programs. This path is ideal for companies with consistent revenue, a solid business plan, and the need for working capital, equipment, or real estate, but not necessarily equity dilution.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    SBA loans are available to most U.S.-based small businesses, including LLCs, C Corporations, and S Corporations. <b>{n}</b>’s legal structure qualifies, provided it meets SBA size standards and is an operating for-profit entity. Maintaining proper corporate documentation and financial statements will be key for SBA eligibility and underwriting approval.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    With <b>{preraise}</b> already secured in pre-capital, <b>{n}</b> demonstrates financial maturity and operating discipline—important to SBA lenders who prioritize repayment capability over high-risk growth. This foundation enhances the company’s credibility in securing a government-backed loan, where historical performance matters more than speculative upside.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    If <b>{n}</b>’s pre-capital is funded via {premarketstr}; an SBA loan offers non-dilutive financing as a complementary capital source. This is especially strategic for asset purchases, payroll support, or expansion, where debt may be more appropriate than giving up equity. SBA lending focuses on operational sustainability and repayment strength.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    If <b>{n}</b> plans to raise <b>{raisegoal}</b>, a portion may be structured through SBA debt (typically capped at $5 million for 7(a) loans). SBA financing can fill capital gaps without triggering equity dilution. However, the company must present a clear use-of-funds breakdown and demonstrate the ability to service loan payments from operating cash flow.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
    SBA financing is not part of traditional capital rounds like Series A or B. Instead, it complements those rounds or serves as alternative capital for growth-stage companies not looking to raise equity. For <b>{n}</b>, this may be suitable for funding equipment, expansion, or refinancing high-interest debt during operational scale-up.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    SBA loans are typically disbursed in lump sums or according to an agreed draw schedule, rather than in equity-style tranches. However, draw schedules can still align with project phases (e.g., construction or inventory cycles). <b>{n}</b> should align disbursement requests with project milestones and cash flow needs.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    SBA funds are highly versatile and can be used for:
    - Working capital
    - Equipment or machinery
    - Commercial real estate purchases or improvements
    - Debt refinancing
    Business acquisition (in some cases)
    <b>{n}</b> must clearly articulate fund deployment and its impact on growth or operational stability to meet SBA underwriting standards.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Compared to equity financing, SBA loans shift risk back to the business in the form of guaranteed repayment. While interest rates are favorable, SBA borrowers must demonstrate repayment capacity, personal guarantees, and often collateral. For <b>{n}</b>, this means emphasizing cash flow, historical performance, and responsible financial management.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    SBA financing is typically less expensive than equity in the long run, with interest rates ranging from Prime + 2.75% to 6.5%, depending on the program. There is no dilution, but there is debt service. For <b>{n}</b>, this offers cost certainty, though total repayment may span 7–25 years depending on loan type.
    </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    SBA loan costs include packaging fees, guarantee fees (up to 3.75%), and legal fees, often totaling between $500 to $2,500 depending on loan size and complexity. If <b>{n}</b> has a {upfrontcost}, {costanalysis}
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    The typical timeframe for receiving SBA financing ranges from 4 weeks to 10 weeks. The process involves submitting an application, completing necessary documentation, and undergoing a thorough review. {timeanalysis}</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime,costanalysis=costanalysis,timeanalysis=timeanalysis,premarketstr=premarketStr))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)