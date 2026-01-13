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


def commercialbanking(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><b><u>Definition of Capital Market: Commercial Banking</b></u></p>
    
    <p><b><u>Introduction</u></b><br>
    Commercial banking is ideal for companies seeking debt capital—typically through term loans, lines of credit, or equipment financing—in amounts ranging from $50,000 to several million dollars, depending on the business’s financial profile. It is designed for established businesses with steady revenue, strong credit, and the capacity to repay borrowed funds over time. {n} fits that definition. Commercial banking has been a core funding source for businesses for decades. For example, in the first half of 2024, U.S. commercial banks issued over $85 billion in new small business loans. In 2023, businesses accessed over $150 billion in commercial credit through banks, with the average small business loan falling between $250,000 and $500,000. The average interest rate for small business loans from commercial banks ranged from 6.25% to 9.5%, depending on loan structure and borrower risk profile. The primary risk of commercial banking is the obligation to repay debt regardless of business performance, which can strain cash flow or lead to default if revenue dips. There are nine types commercial banking options you can match with: 1) Acquisition Loan, 2) Asset Based Lending, 3) Collaterized Debt, 4) Commercial Bank Loan (4135), 5) Credit Card, 6) Equipment Loan, 7) Line of Credit, 8) Real State Loan, 9) Standby Lines of Credit. We will matcch you with best Commercial Banking loan for your business as per your need. 
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br>1. Commercial banking refers to the financial services provided by banks to businesses and corporations, primarily focused on offering loans, credit, deposit accounts, and cash management solutions. These banks serve as intermediaries between businesses and the capital they need to operate and grow, offering products such as term loans, lines of credit, equipment financing, and treasury services. Unlike investment banks, which deal with securities and mergers, commercial banks focus on day-to-day financial operations and short- to medium-term funding needs. They assess a company’s creditworthiness, cash flow, and collateral to structure repayment terms and interest rates. Commercial banking plays a critical role in supporting business expansion, liquidity, and financial stability, particularly for small to mid-sized enterprises. (Kagan, 2024)
<br>
    <br>2. There are several types of commercial banking services available to companies, each tailored to meet different financial needs based on the size and stage of the business. Retail commercial banks serve small to mid-sized businesses with basic financial products like checking accounts, small business loans, and lines of credit. Corporate or wholesale banks cater to large enterprises, offering more complex services such as syndicated loans, treasury and cash management, and foreign exchange solutions. Investment arms within commercial banks may also offer services like capital raising or advisory for mergers and acquisitions. Additionally, community banks often support local businesses with personalized service and more flexible lending terms, while online commercial banks provide digital-first options with lower overhead and potentially more competitive rates. Each type plays a distinct role in helping companies manage liquidity, fund growth, and optimize financial operations. (Ipb, 2024)
<br>
    <br>3. The history of commercial banking dates back thousands of years, with its earliest roots in ancient Mesopotamia, where merchants provided loans to farmers and traders. Over time, this evolved through ancient Greece and Rome, where rudimentary banking systems managed deposits and credit. In the Middle Ages, Italian city-states like Florence and Venice became hubs for early banking institutions such as the Medici Bank, which helped formalize modern banking practices. Commercial banking as we know it began taking shape in the 17th and 18th centuries, with the founding of institutions like the Bank of England (1694), which helped regulate currency and lend to governments and businesses. During the Industrial Revolution, banks played a critical role in financing factories, railroads, and trade expansion. In the U.S., commercial banking developed rapidly after the National Banking Act of 1863 and evolved through regulations like the Federal Reserve Act (1913) and the Glass-Steagall Act (1933), which shaped the modern banking system. Today, commercial banks are central to global economic growth, offering businesses a wide range of financial services to manage cash, secure credit, and scale operations. (World History, 2025)
<br>
    <br>4. For companies, commercial banking carries several key risks that can impact financial health and operational flexibility. The most significant risk is debt repayment pressure—businesses that take out loans or lines of credit must repay them on a fixed schedule, even during periods of reduced revenue or unexpected challenges. High interest rates, especially on variable-rate loans, can increase borrowing costs over time, making it harder to maintain profitability. If a company uses its assets as collateral, defaulting on a loan could result in the loss of critical equipment or property. Additionally, banks may impose restrictive loan covenants, limiting a company’s financial decisions or strategic flexibility. Overreliance on debt from commercial banks can also make a business more vulnerable to economic downturns, tightening credit conditions, or shifts in banking policies. For small or early-stage companies, access to commercial banking services may also be limited by credit history or insufficient collateral, compounding these risks. (Staff, 2023)
<br>
    <br>5. To raise capital through commercial banking, a company must meet certain financial and operational criteria that demonstrate its ability to repay debt. First, the business needs to have a strong credit history, as banks assess past borrowing behavior to determine creditworthiness. Solid financial statements, including balance sheets, profit and loss statements, and cash flow reports, are essential to show the bank that the company is financially stable and capable of managing additional debt. Companies also need to provide collateral to secure loans, such as property, equipment, or receivables, in case of default. The business must also demonstrate a clear and viable business plan, explaining how the borrowed capital will be used to generate growth or improve operations. Additionally, banks typically require companies to meet certain covenants, which are conditions that limit certain activities, such as taking on more debt or making large capital expenditures, in order to protect the bank’s investment. Companies seeking larger loans may also need to show a track record of profitability or steady revenue growth, and businesses in the early stages of development may face stricter requirements or higher interest rates due to perceived risk. (Guinan, 2024)
    </p>
                             
    <p><b><u>References</u></b><br>
    <br>Kagan, J. (2024, April 3). How do commercial banks work, and why do they matter? Investopedia. <a href="https://www.investopedia.com/terms/c/commercialbank.asp">https://www.investopedia.com/terms/c/commercialbank.asp</a>
    <br><br>Ipb. (2024, March 7). Types of Commercial Banks: A simplified Overview. Institute of Professional Banking. <a href="https://ipbindia.com/commercial-banks-a-simplified-overview/?">https://ipbindia.com/commercial-banks-a-simplified-overview/?</a>
    <br><br>World History. (2025, March 9). The History of Banking - world history. World History. <a href="https://worldhistoryjournal.com/2025/03/09/the-history-of-banking/?">https://worldhistoryjournal.com/2025/03/09/the-history-of-banking/?</a>
    <br><br>Staff, F. I. (2023, September 10). Risk Management in Commercial lending: Ensuring successful loan outcomes. Funder Intel. <a href="https://www.funderintel.com/post/risk-management-in-commercial-lending-ensuring-successful-loan-outcomes?">https://www.funderintel.com/post/risk-management-in-commercial-lending-ensuring-successful-loan-outcomes?</a>
    <br><br>Guinan, K. (2024, June 27). Business loan requirements: 8 things you will need. Bankrate. <a href="https://www.bankrate.com/loans/small-business/business-loan-requirements/?\">https://www.bankrate.com/loans/small-business/business-loan-requirements/?\</a>
    </p>
    <p><b><u>Qualification Requirements</u></b>
    <br>• Registered Business Entity: The company must be legally registered (LLC, C-Corp, S-Corp).
    <br>• Valid Business License: Necessary licenses and permits must be in place.
    <br>• Tax Identification Number (TIN): A valid EIN/TIN from the IRS is required.
    <br>• Operating Agreement/Bylaws: LLCs or corporations must have proper governance documents.
    <br>• Proof of Good Standing: The company must be current on all legal and financial filings.
    <br>• Compliance with Regulations: Adherence to financial regulations and reporting requirements.
    <br>• Personal Guarantees: Owners may need to provide personal guarantees for smaller businesses.
    <br>• Legal Counsel Involvement: Necessary to ensure compliance with laws in loan agreements.
    <br>• Contracts in Order: Existing contracts must be legally valid and up-to-date.
    <br>• AML and KYC Compliance: Must comply with anti-money laundering and identity verification requirements.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Business Financial Statements:
    <br>Includes balance sheets, income statements, and cash flow statements to demonstrate financial health.
    <br>• Tax Returns:
    <br>Recent tax returns (usually 2-3 years) to verify the company’s income and tax compliance.
    <br>• Business Plan:
    <br>A detailed plan outlining how the borrowed capital will be used and the strategy for repayment.
    <br>• Personal Financial Statements:
    <br>For small businesses or startups, owners may need to provide personal financial statements to demonstrate financial responsibility.
    <br>• Proof of Collateral:
    <br>Documents showing ownership and value of assets offered as collateral (e.g., property deeds, equipment appraisals).
    <br>• Legal Documents:
    <br>Business registration documents, operating agreements (LLCs), or corporate bylaws (C-Corp/S-Corp) to verify legal structure.
    <br>• Debt-Service Coverage Ratio (DSCR):
    <br>A calculation showing the company’s ability to cover debt obligations with its earnings.
    <br>• Credit Reports:
    <br>Both personal and business credit reports to assess creditworthiness.
    <br>• Business Licenses and Permits:
    <br>Proof of necessary licenses and regulatory compliance for the company to operate legally.
    <br>• Ownership and Management Information:
    <br>Details about the ownership structure, key stakeholders, and management team.
    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def commercialbankingfaq(request):
    introduction = mark_safe("""                      
    <p><b><u>FAQs</u></b></p>
   
    <p><b><u>1. What is commercial banking?</u></b><br>
    • Answer: Commercial banking refers to financial institutions that provide services such as loans, deposits, and other banking services to businesses, rather than individuals.
    </p>
                             
    <p><b><u>2. What types of loans do commercial banks offer to businesses?</u></b><br>
    • Answer: Commercial banks offer various types of loans, including term loans, lines of credit, SBA loans, equipment financing, and real estate loans, tailored to businesses’ needs.
    </p>
                             
    <p><b><u>3. What are the requirements for a business to qualify for a loan from a commercial bank?</u></b><br>
    • Answer: Requirements include a strong credit history, financial statements (balance sheet, income statement, cash flow), collateral, a business plan, and personal guarantees in some cases.</p>
                             
    <p><b><u>4. How do commercial banks assess a company’s creditworthiness?</u></b><br>
    • Answer: Banks assess creditworthiness by reviewing the company’s financial health, credit score, debt-service coverage ratio, collateral, and overall business stability.</p>
                             
    <p><b><u>5. Can a startup get a loan from a commercial bank?</u></b><br>
    • Answer: While it can be more challenging for startups, it is possible if the business has a solid business plan, personal guarantees from owners, and collateral. However, some banks may require a longer track record of operations.
    </p>
                             
    <p><b><u>6. What is the interest rate on a commercial loan?</u></b><br>
    • Answer: Interest rates on commercial loans vary depending on the loan type, the company’s creditworthiness, the market rates, and the loan term. Rates can be fixed or variable.</p>
                             
    <p><b><u>7. What is collateral, and why is it required for commercial loans?</u></b><br>
    • Answer: Collateral is an asset, such as real estate, equipment, or inventory, that a company offers to secure a loan. If the business defaults, the bank can seize the collateral to recover the loan amount.</p>
                             
    <p><b><u>8. What is the process of applying for a commercial loan?</u></b><br>
    • Answer: The process typically involves submitting an application with financial documents, business plans, and supporting materials. The bank will then review the information, perform due diligence, and approve or deny the loan.</p>
                             
    <p><b><u>9. What are loan covenants, and how do they impact a business?</u></b><br>
    • Answer: Loan covenants are conditions set by the bank to protect its investment. They can restrict certain business activities (e.g., taking on more debt) and may require the business to meet financial ratios.</p>
                             
    <p><b><u>10. How long does it take to get approved for a commercial loan?</u></b><br>
    • Answer: Loan approval can take anywhere from a few weeks to a few months, depending on the complexity of the loan, the bank’s procedures, and how quickly the company provides the required documentation.</p>

    <p><b><u>11. Can a business apply for multiple Commercial loans at the same time?</u></b><br>
    • Answer: Yes, but businesses should carefully consider their capacity to manage multiple loans and avoid overextending themselves.</p> 

    <p><b><u>12. What are the fees associated with commercial loans?</u></b><br>
    • Answer: Fees may include application fees, origination fees, processing fees, and prepayment penalties. It’s important for companies to review the loan terms to understand all potential costs.</p>                                                               
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def commercialbankingtwelve(request):
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
    #Up front Cost options Not required as the require cost ranges between zero to 5000 so every option from user would have the same cost analysis.
#    up_front_cost_options ={
#        'Minimum $0 - Maximum $499' : 'this model remains financially inefficient as more upfront cost might be required for royalty financing deal.',
#        'Minimum $500 - Maximum $999' :  'this model remains financially inefficient as more upfront cost might be required for royalty financing deal.',
#        'Minimum $1000 - Maximum $2499' :  'this model remains financially inefficient as more upfront cost might be required for royalty financing deal.',
#        'Minimum $2500 - Maximum $4999' :  'this model remains financially efficient however more upfront cost might be required for royalty financing deal.',
#        'Minimum $5000 - Maximum $9999' :  'this model remains financially efficient and founder friendly.',
#        'Minimum $10000 - Maximum $24999' : 'this model remains financially efficient and founder friendly.',
#        'Minimum $25000 - Maximum $49999' : 'this model remains financially efficient and founder friendly.',
#        'More than $50000+' : 'this model remains financially efficient and founder friendly.',             
#    }
#    costanalysis = up_front_cost_options[upfrontcost]

    #Up front Cost options
    up_front_time_options ={
        '1 Day to 1 Week' : 'might not be enough to go through the process to get a commercial bank loan.',
        '1 Week to 2 Week' : 'might not be enough to go through the process to get a commercial bank loan.',
        '2 Weeks to 4 Weeks' : 'aligns with raising funds using commercial bank loan.',
        '1 Month to 2 Months' : 'aligns with raising funds using commercial bank loan.',
        '2 Months to 3 Months' : 'aligns with raising funds using commercial bank loan.',
        '3 Months to 6 Months' : 'aligns with raising funds using commercial bank loan.',
        '6 Months to 12 Months' : 'aligns with raising funds using commercial bank loan.',
        'More than 1 year' : 'aligns with raising funds using commercial bank loan.',             
    }
    timeanalysis = up_front_time_options[upfronttime]

    for num,item in enumerate(premarket):
        if num == 0:
            premarketStr = premarketStr + str(item).lower()
        elif num == (len(premarket)-1):
                premarketStr = premarketStr +', and ' + str(item).lower()
        else:        
            premarketStr = premarketStr +', ' + str(item).lower()

    introduction = """
    <p><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Commercial Banking</p>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    Commercial banking capital—primarily in the form of term loans, lines of credit, equipment financing, and SBA loans—is best suited for startups and small businesses that have entered the {stage} stage or can provide collateral and financial projections. While early-stage businesses can qualify for certain products like SBA 7(a) startup loans, traditional banks generally require:
    <br><br>• A registered business entity with at least 6–12 months of operating history
    <br>• Creditworthy founders or guarantors
    <br>• A well-documented business plan with financial projections
    <br>• Proof of cash flow or asset coverage for loan repayment
    <br><br>For {n}, commercial banking is most viable post-revenue or at early commercialization—particularly when working capital, inventory, or equipment funding is needed.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Commercial lenders typically require a U.S.-registered, for-profit legal entity—preferably an LLC or C Corporation—with a clear operational history, employer identification number (EIN), and business bank account.
    <br>If {n} is a sole proprietorship or recently incorporated, it may face more scrutiny or require a personal guarantee from founders. A robust business credit profile and clean corporate structure (e.g., operating agreements, licenses, tax ID) will significantly enhance bankability.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    If {n} has secured {preraise} in equity or grant-based pre-capital, it strengthens the case for creditworthiness. While commercial banks focus primarily on repayment capacity, early-stage capital shows investor validation and enhances liquidity.
<br>
    <br>Additionally, banks will evaluate:
    <br>• Cash balances and burn rate
    <br>• Monthly recurring revenue (if any)
    <br>• Personal credit history of founders
    <br>• Debt-to-income ratios and DSCR (debt service coverage ratio)
    <br><br>Pre-capital strengthens leverage when negotiating with commercial lenders and can be paired with secured credit products.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    If {n}’s initial capital was sourced from {premarketstr};commercial lenders may require subordination of those investments or seek additional collateral/security for loan approval. However, equity backing can help offset operational risk and provide a “capital cushion” that banks appreciate when considering repayment risk.
    <br><br>Lenders are particularly favorable toward companies that demonstrate:
    <br>• Investor diversity
    <br>• Non-dilutive funding (grants, R&D credits)
    <br>• Healthy cap tables without excessive founder dilution
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    If {n} intends to raise {raisegoal} over the next 12–18 months, commercial loans can act as bridge capital or working capital lines, especially if used to:
    <br>• Cover receivables gaps
    <br>• Purchase inventory or equipment
    <br>• Fund operational growth or expansion
    <br>
    <br>Typical commercial banking products range from:
    <br>• $50K–$5M for SBA or secured term loans
    <br>• $100K–$1M for revolving credit lines
    <br>• Up to $500K for equipment financing
    <br><br>Blending debt with equity reduces dilution and improves capital efficiency for milestone-based fundraising strategies.
    </p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Commercial debt is non-dilutive and complements equity capital by offering short-to-mid-term financing options. For {n}, banking capital is best positioned between pre-seed and Series A, when:
    <br><br>• The company has sufficient recurring revenue or signed contracts
    <br>• Near-term cash needs are tactical (e.g., hiring, equipment, marketing)
    <br>• Founders seek to preserve equity for future priced rounds
    <br><br>Debt financing through commercial banking should be used to extend runway or fund capital-efficient growth, not to cover unsustainable burn.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Bank loans and credit lines are typically disbursed in one of the following formats:
    <br><br>• Term loans: Lump sum disbursed upfront with a fixed repayment schedule
    <br>• Lines of credit: Drawn as needed with interest charged only on usage
    <br>• SBA loans: Lump sum or staged depending on the SBA lender agreement
    <br>
    <br>For {n}, aligning loan tranches with working capital needs and revenue cycles will optimize use without over-leveraging.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Commercial capital is best applied to predictable and revenue-generating activities, including:
    <br><br>• Hiring or payroll expansion
    <br>• Inventory or raw material purchases
    <br>• Equipment or hardware upgrades
    <br>• Leasehold improvements or relocation
    <br>• Marketing and customer acquisition
    <br><br>Lenders will require a detailed use-of-funds breakdown and may place covenants on capital usage, especially for larger facilities.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Commercial banking capital carries low dilution risk but moderate repayment and liquidity risk, particularly if:
    <br><br>• Revenues are inconsistent or seasonal
    <br>• Founders lack personal collateral or credit history
    <br>• Economic conditions (e.g., interest rates, inflation) tighten credit access
    <br><br>Risk mitigation for {n} includes:
    <br><br>• Building a 12-month cash flow forecast
    <br>• Keeping debt service ratios above 1.25x
    <br>• Avoiding personal guarantees where possible
    <br>• Maintaining compliance with all covenants and financial reporting
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    Commercial loans are cost-effective compared to equity, typically with:
    <br><br>• Interest rates ranging from 5%–12% APR (depending on credit, product, and collateral)
    <br>• Origination fees (0.5%–3%)
    <br>• Minimal equity impact unless using convertible debt
    <br><br>The true cost of capital is lower than venture equity in the long term, especially for businesses with high gross margins and recurring revenue.
    </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    Upfront costs for commercial banking capital may include:
    <br><br>• Loan origination or underwriting fees
    <br>• Legal costs for collateral agreements or UCC filings
    <br>• Appraisal or inspection fees for equipment/real estate-backed loans
    <br>• Business plan preparation or CPA-reviewed financials
    <br><br>Genrally, cost for commercial banking ranges between $0 to $5000. If {n} has a {upfrontcost} allocated to debt readiness (e.g., legal, financial modeling, DUNS credit profile setup), commercial funding can provide rapid scale-up capital—especially when compared to slower-moving equity negotiations.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    The commercial lending process typically follows this timeline:
    <br><br>• Application to underwriting: 1–3 weeks
    <br>• Underwriting to approval: 1–2 weeks
    <br>• Closing to funding: 1 week (longer for SBA loans)
    <br>Total timeline: 1–4 weeks (standard), 4–10 weeks (for SBA)
    <br><br>To maximize success, {n} should:
    <br>• Prepare 2 years of financials (projected and historical if available)
    <br>• Maintain strong personal and business credit scores
    <br>• Build relationships with local bank reps or SBA lenders
    <br>• Compare multiple term sheets (regional banks, online lenders, credit unions)
    <br><br> Initial timing required by {n} of {upfronttime} {timeanalysis} 
    </p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime,timeanalysis=timeanalysis,premarketstr=premarketStr))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)