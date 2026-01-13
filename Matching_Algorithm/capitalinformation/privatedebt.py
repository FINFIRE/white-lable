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


def privatedebt(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><b><u>Definition of Capital Market: Private Debt</b></u><br></p>
    
    <p><b><u>Introduction</u></b><br>
    Private debt is an ideal capital-raising tool for companies seeking flexible, non-dilutive financing typically ranging from $1 million to $100 million, depending on the company’s size, cash flow, and creditworthiness. Private debt allows businesses to raise capital without giving up equity, making it a preferred route for companies with stable revenue and a clear repayment plan. {n} fits this profile, given its operating history and projected cash flow. Private debt has emerged as a reliable source of funding over the past decade, especially in times of tighter bank lending. For example, in 2023, private debt fundraising reached $210 billion globally, demonstrating the growing confidence in this asset class. The private debt market’s total assets under management exceeded $1.6 trillion in 2023, and it continues to grow as more institutional investors seek yield. On average, private debt transactions in 2023 ranged between $10 million and $50 million, depending on sector and deal structure. However, risks include high interest costs, strict covenants, and the potential for default if projected cash flows fall short.  There are eight types of Private Debt that we can match you with: 1) Acquisition Loan, 2) Asset Based Lending, 3) Bridge Financing, 4) Collateralized Debt, 5) Hard Money Loan, 6) Private Debt, 7) Promissory Note, 8) Real Estate Loan. We will select the most appropriate type as per your business need.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br>1. Private debt refers to loans or credit extended to companies by non-bank lenders such as private equity firms, institutional investors, or specialized debt funds, rather than through traditional public markets or banks. It typically involves direct lending agreements negotiated privately between the borrower and the lender, offering more flexible terms than traditional bank financing. Common forms of private debt include mezzanine financing, direct lending, unitranche loans, and distressed debt. This type of capital is especially useful for middle-market companies seeking to fund growth, acquisitions, or restructuring without giving up equity ownership. Private debt has become an increasingly important alternative financing source, especially as regulatory constraints have limited traditional bank lending. (Team, 2025)
<br>
    <br>2. Private debt encompasses a range of non-bank, privately negotiated lending arrangements that provide capital to companies without issuing equity. The primary types of private debt include direct lending, mezzanine financing, distressed debt, venture debt, and special situations. Direct lending involves private lenders providing senior secured loans to mid-market companies, typically for acquisitions or refinancing. Mezzanine financing is a hybrid of debt and equity, offering subordinated debt with higher yields and potential equity upside. Distressed debt refers to investing in the debt of financially troubled companies, often with the aim of gaining control through restructuring. Venture debt supports high-growth startups that already have venture capital backing but need additional runway without further dilution. Lastly, special situations include unique or opportunistic lending circumstances like litigation finance or asset-backed lending. These varied strategies allow institutional investors to target different risk-return profiles and capital needs. (Knickerbocker, 2025)
<br>
    <br>3. The history of private debt as an asset class began gaining traction in the aftermath of the 2008 global financial crisis, when traditional banks faced tighter regulations and stricter lending requirements under frameworks like Basel III. This created a funding gap for small and mid-sized enterprises (SMEs), which alternative lenders and private funds stepped in to fill. However, the roots of private debt stretch back further to the leveraged buyout boom of the 1980s, when mezzanine and subordinated debt instruments first gained popularity. The asset class matured in the 2010s, with institutional investors such as pension funds, insurance companies, and sovereign wealth funds seeking stable, risk-adjusted returns amid a low-interest-rate environment. By the 2020s, private debt had firmly established itself as a core part of the alternative investment landscape, with assets under management exceeding $1.6 trillion globally. (FS Investments, 2024)
<br>
    <br>4. Private debt carries several key risks that both companies and investors should be aware of. For companies, the primary risk is the obligation to repay fixed debt regardless of business performance, which can strain cash flow—especially during downturns. Unlike equity financing, private debt must be repaid with interest, increasing financial pressure. For lenders and investors, risks include borrower default, lack of liquidity (as private debt is not typically traded on public markets), and limited transparency due to the private nature of the transactions. Additionally, private debt is often used in leveraged situations, which can amplify losses if the borrower’s business underperforms. Changes in interest rates or economic conditions can also affect the value and repayment prospects of these loans. (Edlich, 2025)
<br>
    <br>5. To raise capital via private debt, a company must typically meet several key requirements to attract lenders and ensure credibility. First, the business should have a solid operating history and proven cash flow, as lenders seek assurance that the company can meet its debt obligations. A strong credit profile, including a good credit score and low existing debt-to-equity ratio, is also essential. Companies are usually required to present detailed financial statements—such as income statements, balance sheets, and cash flow projections—as well as a clearly defined use of proceeds. Legal incorporation, compliance with regulatory requirements, and sometimes collateral (such as assets or receivables) are also necessary. While early-stage companies can access private debt in some cases, most lenders prefer more mature businesses with established revenues and a clear path to profitability. Additionally, having a robust business plan and demonstrating risk mitigation strategies can further increase a company’s chances of securing private debt funding. (SEC, n.d.)
    </p>
                             
    <p><b><u>References</u></b><br>
    <br>Team, A. (2025, January 8). What is private debt? Allvue Systems. <a href="https://www.allvuesystems.com/resources/what-is-private-debt/">https://www.allvuesystems.com/resources/what-is-private-debt/</a>
<br>
    <br>Knickerbocker, K., & Martinez, R. (2025, January 30). Private debt: The ultimate guide (2024) | PitchBook - PitchBook. PitchBook. <a href="https://pitchbook.com/blog/what-is-private-debt">https://pitchbook.com/blog/what-is-private-debt</a>
<br>
    <br>FS Investments. (2024, April 25). Awakening: The rise of private debt | FS Investments. <a href="https://fsinvestments.com/fs-insights/awakening-the-rise-of-private-debt/">https://fsinvestments.com/fs-insights/awakening-the-rise-of-private-debt/</a>
<br>
    <br>Edlich, A., Croke, C., Dahlqvist, F., & Teichner, W. (2025, February 13). Global Private Markets Report 2025: Private equity emerging from the fog. McKinsey & Company. <a href="https://www.mckinsey.com/industries/private-capital/our-insights/global-private-markets-report">https://www.mckinsey.com/industries/private-capital/our-insights/global-private-markets-report</a>
<br>
    <br>SEC.gov | Private Companies and the SEC. (n.d.). <a href="https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/private-companies-sec">https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/private-companies-sec</a>
    </p>
                             
    <p><b><u>Qualification Requirements</u></b>
    <br>• Registered Business – Must be a legal entity like an LLC or corporation in good standing.
    <br>• Securities Compliance – Must follow SEC rules, usually via a Regulation D exemption.
    <br>• Accredited Investors – Often required to verify investors meet SEC’s accredited investor criteria.
    <br>• Disclosure Document (PPM) – A formal memo is typically used to outline the offer’s terms and risks.
    <br>• State Law Compliance – Must meet “Blue Sky” laws in each state where debt is offered.
    <br>• Formal Debt Agreement – Need legal instruments like promissory or convertible notes.
    <br>• Internal Approval – Board or owners must authorize the fundraising.
    <br>• Financial Records – Accurate financials and projections must be available.
    <br>• Use of Funds Statement – Clear explanation of how the borrowed funds will be used.
    <br>• Legal Support – Should have legal counsel to ensure full compliance and proper documentation.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Private Placement Memorandum (PPM)
    <br>• Debt Instrument (Note/Agreement)
    <br>• Subscription Agreement
    <br>• Accredited Investor Questionnaire
    <br>• Pitch Deck or Business Plan
    <br>• Recent Financial Statements
    <br>• Use of Proceeds Summary
    <br>• Cap Table (Ownership Structure)
    <br>• Incorporation & Legal Docs
    <br>• Board Resolution Authorizing Debt Raise
    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privatedebtfaq(request):
    introduction = mark_safe("""                     
    <p><b><u>FAQs</u></b></p>
                             
    <p><b><u>1. What is private debt?</u></b><br>
    • Answer: Private debt refers to debt financing that is provided by private investors or financial institutions, rather than through traditional public debt markets. It typically includes loans, bonds, or credit facilities offered to companies in exchange for interest payments and principal repayment over time.
    </p>
                             
    <p><b><u>2. Who can raise capital through private debt?</u></b><br>
    • Answer: Private debt is generally available to companies that are beyond the startup phase and have a proven business model with established revenue and cash flow. These companies typically need to demonstrate the ability to repay the debt.
    </p>
                             
    <p><b><u>3. What are the types of private debt available?</u></b><br>
    • Answer: The main types of private debt include:
    <br>- Senior debt: The most secure form of debt with priority in repayment.
    <br>- Subordinated debt: Higher risk and interest rates, repaid after senior debt in case of liquidation.
    <br>- Mezzanine financing: A mix of debt and equity financing, often used for growth-stage companies.
    <br>- Unitranche debt: Combines senior and subordinated debt into a single loan.
    </p>
                             
    <p><b><u>4. How much capital can a company raise through private debt?</u></b><br>
    • Answer: Companies can raise anywhere from $500,000 to $50 million, depending on their size, financial health, and the type of debt being issued.
    </p>
                             
    <p><b><u>5. What are the benefits of private debt?</u></b><br>
    • Answer: Benefits include access to capital without diluting equity, flexibility in structuring debt, and the ability to use the funds for growth, acquisitions, or refinancing. Private debt also provides companies with faster access to capital compared to public markets.
    </p>
                             
    <p><b><u>6. What are the risks of private debt?</u></b><br>
    • Answer: The main risks of private debt are the obligation to repay the debt with interest regardless of business performance, the potential for default, and the risk of damaging relationships with lenders if repayment terms are not met. If the company’s cash flow declines, it could face serious financial stress.
    </p>
                             
    <p><b><u>7. How does private debt differ from venture capital or equity financing?</u></b><br>
    • Answer: Unlike venture capital or equity financing, private debt does not involve giving up ownership or control of the company. However, it does require the company to repay the debt with interest, which can be a financial burden if cash flow is not strong.
    </p>
                             
    <p><b><u>8. What are the typical interest rates for private debt?</u></b><br>
    • Answer: Interest rates for private debt can range from 5% to 15%, depending on the risk profile of the company, the amount of debt raised, and the type of loan. The rates are generally higher than those for traditional bank loans due to the higher risk involved.
    </p>
                             
    <p><b><u>9. How long does it take to secure private debt financing?</u></b><br>
    • Answer: The process of securing private debt can take anywhere from 30 days to 6 months, depending on the complexity of the transaction and the due diligence process.</p>
                             
    <p><b><u>10. What are the eligibility requirements for private debt?</u></b><br>
    • Answer: To be eligible for private debt, a company typically needs to have:
    <br>- A proven business model with steady revenue.
    <br>- A track record of profitable operations or clear growth potential.
    <br>- A strong management team and financial reporting systems.
    <br>- The ability to repay the debt over the agreed period.
    </p>

    <p><b><u>11. Can startups raise private debt?</u></b><br>
    • Answer: Startups typically do not qualify for private debt as they may lack the revenue and cash flow to support repayment. Private debt is generally better suited for established companies with stable financials and a proven ability to generate cash flow.</p>

    <p><b><u>12. How does a company repay private debt?</u></b><br>
    • Answer: Repayment terms for private debt can vary but typically involve regular interest payments (quarterly or semi-annually) and a lump sum repayment of the principal at the end of the loan term. The repayment schedule will be outlined in the loan agreement.</p>                                            
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privatedebttwelve(request):
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
    premarketStr = ''

    #Up front Cost options
    up_front_cost_options ={
        'Minimum $0 - Maximum $499' :'private debt is an efficient option but the cost sometime might be inadequate to suffice the fees involved in private debt.',
        'Minimum $500 - Maximum $999' :  'private debt is an efficient option but the cost sometime might be inadequate to suffice the fees involved in private debt.',
        'Minimum $1000 - Maximum $2499' :  'private debt is an efficient option but the cost sometime might be inadequate to suffice the fees involved in private debt.',
        'Minimum $2500 - Maximum $4999' :  'private debt remains an efficient option for growth capital—especially compared to equity raises with higher transaction friction and dilution.',
        'Minimum $5000 - Maximum $9999' :  'private debt remains an efficient option for growth capital—especially compared to equity raises with higher transaction friction and dilution.',
        'Minimum $10000 - Maximum $24999' : 'private debt remains an efficient option for growth capital—especially compared to equity raises with higher transaction friction and dilution.',
        'Minimum $25000 - Maximum $49999' : 'private debt remains an efficient option for growth capital—especially compared to equity raises with higher transaction friction and dilution.',
        'More than $50000+' : 'private debt remains an efficient option for growth capital—especially compared to equity raises with higher transaction friction and dilution.',             
    }
    costanalysis = up_front_cost_options[upfrontcost]

    #Up front Cost options
    up_front_time_options ={
        '1 Day to 1 Week' : 'required time is not a direct match to with this capital market option',
        '1 Week to 2 Week' : 'required time is not a direct match to with this capital market option',
        '2 Weeks to 4 Weeks' : 'required time matches with this option but probability of additional time requirement is high.',
        '1 Month to 2 Months' : 'required time matches with this option',
        '2 Months to 3 Months' : 'required time matches with this option',
        '3 Months to 6 Months' : 'required time matches with this option',
        '6 Months to 12 Months' : 'required time matches with this option',
        'More than 1 year' : 'required time matches with this option',             
    }
    timeanalysis = up_front_time_options[upfronttime]

    entity_options ={
         "None (To be Determined)" : "does not qualify, and additionally it requires the business maintains clean financial statements, active operations, and demonstrates an ability to repay debt. Strong internal governance and compliance practices improve access and lender confidence.",
         "Sole Proprietorship" : "does not qualify, and additionally it requires the business maintains clean financial statements, active operations, and demonstrates an ability to repay debt. Strong internal governance and compliance practices improve access and lender confidence.",
         "LLC" : "qualifies, provided the business maintains clean financial statements, active operations, and demonstrates an ability to repay debt. Strong internal governance and compliance practices improve access and lender confidence." ,
         "LP" : "does not qualify, and additionally it requires the business maintains clean financial statements, active operations, and demonstrates an ability to repay debt. Strong internal governance and compliance practices improve access and lender confidence.",
         "GP" : "does not qualify, and additionally it requires the business maintains clean financial statements, active operations, and demonstrates an ability to repay debt. Strong internal governance and compliance practices improve access and lender confidence.",
         "S Corporation" : "qualifies, provided the business maintains clean financial statements, active operations, and demonstrates an ability to repay debt. Strong internal governance and compliance practices improve access and lender confidence.",
         "C Corp" : "qualifies, provided the business maintains clean financial statements, active operations, and demonstrates an ability to repay debt. Strong internal governance and compliance practices improve access and lender confidence.",
         "Other" : "does not qualify, and additionally it requires the business maintains clean financial statements, active operations, and demonstrates an ability to repay debt. Strong internal governance and compliance practices improve access and lender confidence.",
    }
    entityanalysis = entity_options[entity]

    for num,item in enumerate(premarket):
        if num == 0:
            premarketStr = premarketStr + str(item).lower()
        elif num == (len(premarket)-1):
                premarketStr = premarketStr +', and ' + str(item).lower()
        else:        
            premarketStr = premarketStr +', ' + str(item).lower()    
    introduction = """
    <p><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Private Debt</p>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    As {n} advances into a {stage} stage, private debt financing offers a flexible, non-dilutive way to raise capital—particularly through structured term loans, revenue-based debt, or mezzanine financing. This pathway is ideal for companies with recurring revenue, positive cash flow trends, and a clear capital deployment plan that supports repayment within a defined term.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Private debt is typically available to most U.S.-based for-profit business entities, including LLCs, C Corporations, and S Corporations. {n}’s current legal structure {entityanalysis}, provided the business maintains clean financial statements, active operations, and demonstrates an ability to repay debt. Strong internal governance and compliance practices improve access and lender confidence.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    With {preraise} already secured in pre-capital, {n} shows maturity in financial management and execution. This reduces perceived risk for private lenders, who prioritize cash flow sufficiency and repayment capability over speculative growth. A strong capital foundation can support negotiation of better terms and less stringent covenants.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    If {n}’s pre-capital was funded through {premarketstr} can serve as a complementary non-dilutive layer in the capital stack. It is particularly effective for operational scale-up, M&A transactions, or inventory expansion—scenarios where debt is more suitable than continued dilution through equity
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    If {n} intends to raise {raisegoal}, private debt can account for a significant portion—often between $500,000 and $25 million depending on revenue, EBITDA, and asset base. Lenders will require detailed financial projections, a defined use-of-funds plan, and evidence of the company’s ability to service monthly or quarterly debt obligations from operating income.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Private debt is not typically part of a traditional capital round (e.g., Series A/B), but instead acts as supplemental or bridge financing. For {n}, private debt can fund capital expenditures, refinance existing obligations, or extend the runway between equity raises—without affecting valuation or control.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Private debt is commonly issued in a lump sum, though larger facilities may allow multiple draws based on agreed performance milestones. {n} should plan its draw schedule in alignment with project timelines, revenue cycles, or acquisition closings to optimize cash flow and interest accrual management.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Private debt is versatile and well-suited for uses such as:
    <br>- Working capital
    <br>- Growth marketing and customer acquisition
    <br>- Equipment purchases
    <br>- Business expansion or M&A
    <br>- Refinancing of existing debt
    <br>Lenders will require a comprehensive deployment plan demonstrating how the borrowed funds will contribute to revenue growth and/or operational stability.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Private debt introduces repayment obligations and often requires personal guarantees, cash flow covenants, or liens on assets. Unlike equity, the risk is borne by the business in the form of scheduled repayments regardless of growth. For {n}, this means careful attention to forecasted cash flow, debt service coverage, and contingency planning is critical to mitigate default risk.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    Private debt can carry interest rates from 8% to 18% annually, depending on risk, collateral, and credit profile. Though often more expensive than SBA loans, it is typically cheaper than equity in the long term due to zero dilution. For {n}, private debt offers a predictable cost structure and allows founders to retain full ownership and board control.
    </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    Upfront costs for private debt include origination fees (1–3%), legal expenses, and potential diligence or advisory costs. Total fees can range from $0 to $5,000, depending on deal size and complexity. If {n} has a {upfrontcost} allocated, {costanalysis}
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    Private debt transactions typically close within 2–10 weeks, depending on the lender, documentation readiness, and complexity of the transaction. {n} can expedite the process by preparing:
    <br>- Updated financial statements (preferably audited or reviewed)
    <br>- Revenue and cash flow projections
    <br>- Organizational documents
    <br>- Historical debt schedule and repayment history
    <br>Working with experienced legal counsel and specialized private lenders or placement agents can help streamline execution.
    <br> {timeanalysis}
    </p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime,costanalysis=costanalysis,entityanalysis=entityanalysis,premarketstr=premarketStr,timeanalysis=timeanalysis))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)