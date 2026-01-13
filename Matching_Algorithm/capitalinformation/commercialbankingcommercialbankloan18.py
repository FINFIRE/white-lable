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


def commercialbankingcommercialbankloan(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Commercial Bank Loans</center></p>
    <p><b><u>Introduction</u></b><br>
    Commercial and industrial loans granted by U.S. commercial banks amounted to approximately
    <a href="https://www.statista.com/statistics/1121862/commercial-loans-usa-monthly/">2.8 trillion U.S. dollars from January to April in 2024.</a></p>

    <p><b><u>Definition of Capital Type</b></u><br> 
    1) Commercial loans are the most common loan application through a traditional bank. This is a
    debt-based funding arrangement that a business can set up with a financial institution.
    Commercial loans may be used to fund large capital expenditures or operations that a business
    may otherwise be unable to afford. The challenge is that most businesses must have three years
    of positive growth and profit in the profit and loss statements with strong credit, collateral and
    proof of ability to repay. (Smith, 2021)</p>
                             
    <p>2) A commercial bank loan for business capital is a debt-based financing arrangement where a
    business borrows money from a commercial bank to fund its operations, including major capital
    expenditures or covering operational costs, typically requiring collateral like property or
    equipment and repaid over a set period with interest, allowing the business to access funds
    needed for growth and day-to-day activities that might not be readily available through other
    means; essentially, it's a loan specifically designed for businesses to access capital for business
    purposes. (Kenton, 2020)</p>
                             
    <p>3) A commercial bank loan is a common form of debt financing that businesses use to raise
    capital for activities such as expansion, purchasing equipment, or covering working capital
    needs. These loans can be secured with collateral or unsecured, and typically involve borrowing
    a lump sum that is repaid with interest over a set period. To qualify, businesses must have a legal
    structure, a solid business plan, strong credit, and in some cases, collateral. The advantages of
    commercial bank loans include no ownership dilution, predictable payments, and relatively low
    interest rates. However, businesses must meet stringent qualification criteria and manage the loan
    responsibly to avoid default. Common types of commercial bank loans include term loans, lines
    of credit, SBA loans, and equipment financing. (N/A, n.d.)</p>
                             
    <p>4) A commercial loan is a form of credit that is extended to support business activity. Examp
    les include operating lines of credit and term loans for property, plant and equipment (PP&E).
    While there are a few exceptions (including commercial property owned by an individual), the
    overwhelming majority of commercial loans are extended to business entities like corporations
    and partnerships.<br>
    Private businesses that have financing needs generally borrow from a commercial bank or credit
    union; however, they may also seek credit from equipment finance (leasing) firms or other
    private, non-bank lenders (like factoring companies). There are many forms of credit available to
    support businesses including: Lines of Credit, Term Loans, Capital Leases, Commercial
    Mortgages and Acquisition Loans.<br>
    Most lenders don’t extend credit in perpetuity or without some very specific purpose for the
    funds being advanced. This is what bankers often refer to as loan structure (or credit structure).
    Whether it’s a firm’s business banking division or its commercial real estate lending team
    underwriting the exposure, commercial loan structure is often guided by predetermined credit
    policies. Most commercial loans extended by traditional financial institutions are secured by
    collateral. (Peterdy, n.d.)</p>
                             
    <p>5) Commercial loans are granted to a variety of business entities, usually to assist with short-term
    funding needs for operational costs or for the purchase of equipment to facilitate the operating
    process. In some instances, the loan may be extended to help the business meet more basic
    operational needs, such as funding for payroll or to purchase supplies used in the production and
    manufacturing process.<br>
    These loans often require that a business posts collateral, usually in the form of property, plant or
    equipment that the bank can confiscate from the borrower in the event of default or bankruptcy.
    Sometimes cash flows generated from future accounts receivable are used as a loan's collateral.
    Mortgages issued to commercial real estate are one form of commercial loan. (James, 2020)</p>
                             
    <u><b><p>References</u></b><br>
    James, M. (2020, November 14). Commercial Loan: What It Is, How It Works, Different Types.
    Retrieved from Investopedia: <a href="https://www.investopedia.com/terms/c/commercial-loan.asp">https://www.investopedia.com/terms/c/commercial-loan.asp</a></p>
                             
    <p>Kenton, W. (2020, November 14). Commercial Loan: What It Is, How It Works, Different Types.
    Retrieved from Investopedia:<a href="https://www.investopedia.com/terms/c/commercial-loan.asp"> https://www.investopedia.com/terms/c/commercial-loan.asp</a></p>
                             
    <p>N/A. (n.d.). What Is a Commercial Loan? Retrieved from Liquidity:
    <a href="https://www.liquidity.com/resource-funding/what-is-a-commercial-loan-2">https://www.liquidity.com/resource-funding/what-is-a-commercial-loan-2</a></p>
                             
    <p>Peterdy, K. (n.d.). Commercial Loan. Retrieved from Corporate Finance Institute :
    <a href="https://corporatefinanceinstitute.com/resources/commercial-lending/commercial-loan/">https://corporatefinanceinstitute.com/resources/commercial-lending/commercial-loan/</a></p>
                             
    <p>Smith, T. D. (2021). Business 
    Capital 101. Imaginary Press .
    </p>
                             
    <p>3)Purchasers of securities offered pursuant to Rule 506 receive “restricted” securities, meaning
    that the securities cannot be sold for at least six months or a year without registering them.
    506(c)’s defining feature: A GP can perform general solicitation and advertising without any
    limitation on how much capital they can raise.</p>
                             
    <p><u><b>Legal Qualification Requirements</u></b>
    <br>• Legal Business Structure: The business must be legally registered as a recognized entity
    (e.g., Corporation, LLC, Partnership, Sole Proprietorship).
    <br>• Business License and Permits: The business must hold all required licenses and permits
    to operate legally in its industry and location.
    <br>• Employer Identification Number (EIN): The business must have a valid EIN issued by
    the IRS for tax reporting and identification purposes.
    <br>• Legal Compliance and Good Standing: The business must be in good standing with state
    and federal authorities, including filing tax returns and keeping up with state business
    registration filings.
    <br>• No Pending Legal Issues: The business must not have unresolved legal issues, such as
    lawsuits, judgments, or unpaid liabilities that could impact the loan application.
    <br>• Ownership Documentation: The business must provide clear documentation of
    ownership and control (e.g., articles of incorporation, operating agreements, shareholder
    agreements).
    <br>• Contractual Ability: The business must have the legal authority to borrow funds and enter
    into contractual obligations, as indicated by its governing documents.
    <br>• Intellectual Property Protection (if applicable): The business must have protection for its
    intellectual property (e.g., patents, trademarks, copyrights) if relevant, and may need to use it as
    collateral.
    <br>• Debt Covenants Compliance: The business must comply with any existing debt
    covenants if it has outstanding loans or other financial obligations.
    <br>• Legal Liability Insurance: The business may be required to have adequate legal liability
    insurance, especially if it operates in a high-risk industry.
    <br>• Compliance with Environmental and Zoning Laws (if applicable): The business must• Legal Business Structure: The business must be legally registered as a recognized entity
    (e.g., Corporation, LLC, Partnership, Sole Proprietorship).
    <br>• Business License and Permits: The business must hold all required licenses and permits
    to operate legally in its industry and location.
    <br>• Employer Identification Number (EIN): The business must have a valid EIN issued by
    the IRS for tax reporting and identification purposes.
    <br>• Legal Compliance and Good Standing: The business must be in good standing with state
    and federal authorities, including filing tax returns and keeping up with state business
    registration filings.
    <br>• No Pending Legal Issues: The business must not have unresolved legal issues, such as
    lawsuits, judgments, or unpaid liabilities that could impact the loan application.
    <br>• Ownership Documentation: The business must provide clear documentation of
    ownership and control (e.g., articles of incorporation, operating agreements, shareholder
    agreements).
    <br>• Contractual Ability: The business must have the legal authority to borrow funds and enter
    into contractual obligations, as indicated by its governing documents.
    <br>• Intellectual Property Protection (if applicable): The business must have protection for its
    intellectual property (e.g., patents, trademarks, copyrights) if relevant, and may need to use it as
    collateral.
    <br>• Debt Covenants Compliance: The business must comply with any existing debt
    covenants if it has outstanding loans or other financial obligations.
    <br>• Legal Liability Insurance: The business may be required to have adequate legal liability
    insurance, especially if it operates in a high-risk industry.
    <br>• Compliance with Environmental and Zoning Laws (if applicable): The business must
    comply with zoning laws and environmental regulations, particularly if the loan is for property or
    expansion.
    <br>• U.S. Citizenship or Legal Residency (for U.S. loans): Business owners and key
    personnel may need to be U.S. citizens or legal residents for U.S. loans.</p>
                                 
    <p><b><u>Supporting Document List</u></b>
    <br>• Business Plan: A detailed plan outlining company goals, strategy, target market, and
    Loan Application Form: The formal application for the loan, provided by the bank.
    <br>• Business Plan: A detailed plan outlining company goals, strategy, target market, and
    financial projections.
    <br>• Personal Financial Statements: Detailing assets, liabilities, income, and expenses for
    business owners.
    <br>• Business Financial Statements: Including balance sheet, income statement, and cash flow
    statement (typically for the last 2-3 years).
    <br>• Business Tax Returns: The last 2-3 years of business tax returns.
    <br>• Personal Tax Returns: The last 2-3 years for business owners with substantial ownership.
    <br>• Cash Flow Projections: A 12-month projection of expected cash inflows and outflows to
    demonstrate repayment ability.
    <br>• Bank Statements: Recent business bank statements (typically last 3 to 6 months).
    <br>• Credit Report: Review of the company’s credit history and business/personal credit
    scores of the owners.
    <br>• Collateral Documentation: Documents showing the value and ownership of assets used
    as collateral.
    <br>• Business Structure Documents: Articles of incorporation, partnership agreements, LLC
    operating agreements, or sole proprietorship registration.
    <br>• Licenses and Permits: Copies of relevant business licenses and permits.
    <br>• Contracts or Agreements: Relevant customer, supplier, lease, or other legal agreements.
    <br>• Debt Schedule: A list of all outstanding business debts with terms and balances.
    <br>• Ownership and Management Information: Details about the company’s ownership
    structure and management, including résumés or background of key individuals.
    <br>• Business Insurance Information: Details of the company’s business insurance policies.
    <br>• Market Research or Industry Analysis (Optional): Any additional research or analysis on
    the market or industry, if applicable.
    <br>• Use of Loan Proceeds: A breakdown of how the loan will be used (e.g., equipment,
    expansion, hiring).
    <br>• Loan Covenants (if applicable): Acknowledgment of any loan covenants or conditions
    attached to the loan.                                                                        
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def commercialbankingcommercialbankloanfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Commercial Banking<br>
    Commercial Bank Loans</center></p>                        
    <p><center><u><b>Frequently Asked Question for Commercial Bank Loans</u></b></center></p>
                             
    <p><u><b>1. What is Commercial Bank Loan?</u></b><br>
    •Answer: A commercial bank loan is a form of debt financing provided by banks or financial
    institutions, where the borrower agrees to repay the loan amount, along with interest, over a set
    period of time.</p>
                             
    <p><u><b>2. How does a commercial bank loan differ from other forms of financing?</u></b><br>
    • Answer: Unlike equity financing (which involves selling shares of ownership in your company), a
    commercial bank loan does not require giving up any ownership. However, it involves regular
    repayments with interest and may come with stricter eligibility requirements</p>
                             
    <p><u><b>3. What are the benefits of using a commercial bank loan for my business?</u></b><br>
    • Answer:
    <br>-Preserving Ownership: You don’t have to give up any equity or control over your
    company.
    <br>-Predictable Payments: Fixed monthly payments make budgeting easier.
    <br>-Relatively Low Interest Rates: Commercial banks often offer competitive interest rates,
    especially for established businesses.
    <br>-Flexible Loan Options: Various types of commercial loans can meet different financing
    needs (e.g., term loans, lines of credit).</p>
                             
    <p><u><b>4. What are the potential risks or drawbacks of taking out a commercial bank loan?</u></b><br>
    • Answer:
    <br>-Debt Obligations: Repayment schedules can be burdensome if your business cash flow is
    unstable.
    <br>-Collateral Requirements: Banks may require business or personal assets as collateral,
    which could be at risk if the loan is not repaid.
    <br>-Interest Payments: While rates may be competitive, they still add a financial burden over
    time.
    <br>-Stricter Eligibility Criteria: Banks typically require a strong credit history and solid
    financials.</p>
                             
    <p><u><b>5. What factors do banks consider when approving a commercial loan?</u></b><br>
    • Answer: Banks typically evaluate your business’s creditworthiness, including financial statements
    (e.g., income statement, balance sheet), cash flow, collateral, industry stability, and management
    experience. Your credit score and the length of time your business has been operating also play a
    role.
    </p>
                             
    <p><u><b>6. What types of commercial bank loans are available to my business?</u></b><br>
    • Answer:
    <br>-Term Loans: Fixed loan amounts with a set repayment schedule over a predetermined
    period.
    <br>- Lines of Credit: Flexible borrowing where you can draw funds as needed up to a limit
    and repay them.
    <br>- SBA Loans: Loans backed by the Small Business Administration with more favorable
    terms for small businesses.
    <br>-Working Capital Loans: Short-term loans used for everyday business expenses.
    </p>
                             
    <p><u><b>7. What are the typical interest rates on commercial bank loans?</u></b><br>
    • Answer: Interest rates vary based on factors like your credit score, the type of loan, and the
    economic environment. Rates typically range from 4% to 12%, but higher-risk businesses may
    face higher rates.</p>
                             
    <p><u><b>8. What is the repayment schedule for a commercial bank loan?</u></b><br>
    • Answer: Commercial bank loans usually have fixed monthly payments, with a combination of
    principal and interest. Loan terms can vary from a few months to several years, depending on the
    type of loan.
    </p>
                             
    <p><u><b>9. Can I use a commercial loan for any business purpose?</u></b><br>
    • Answer:Yes, commercial loans can generally be used for a wide range of business purposes, such
    as purchasing equipment, expanding operations, covering working capital needs, or refinancing
    other debts. However, banks may inquire about the purpose of the loan as part of their risk
    assessment. 
    </p>
                             
    <p><u><b>10. How long does it take to get approved for a commercial bank loan?</u></b><br>
    • Answer: The approval process typically takes anywhere from a few days to several weeks,
    depending on the complexity of the loan application, the lender’s requirements, and the speed of
    document processing.
    </p>
                             
    <p><u><b>11. What documents are required when applying for a commercial loan?</u></b><br>
    • Answer: Common documents include financial statements (balance sheet, income statement, cash
    flow statement), business tax returns, personal and business credit reports, business plan, and
    details of collateral, if applicable.
    </p>
                             
    <p><u><b>12. Are there fees associated with commercial bank loans?</u></b><br>
    • Answer: Yes, banks may charge application fees, origination fees, prepayment penalties, or late
    payment fees. It’s essential to fully understand the fee structure before accepting a loan.
    </p>
                             
    <p><u><b>13. What happens if my business cannot repay the loan?</u></b><br>
    • Answer:  If your business fails to meet the repayment terms, the bank may seize collateral (if
    applicable) or take legal action to recover the loan amount. This can have a significant negative
    impact on your credit rating and long-term financial health.</p> 
                             
    <p><u><b>14. How can I improve my chances of getting approved for a commercial loan?</u></b><br>
    • Answer: Maintain strong financial health, have a clear business plan, improve your credit score,
    demonstrate consistent revenue, and be prepared with detailed financial records. Collateral can
    also increase your chances of approval.
    </p>
                             
    <p><u><b>15.  How can a commercial loan help my business grow?</u></b><br>
    • Answer:A well-structured loan can provide the capital needed to scale operations, expand your
    product line, hire more staff, or invest in technology and infrastructure, helping you meet
    business goals and increase profitability.
    </p>

    <p><u><b>16. Can I refinance or modify my loan if my business’s financial situation changes?</u></b><br>
    • Answer: Yes, some commercial bank loans offer refinancing options, which can adjust the terms
    (interest rate, repayment schedule, etc.) if needed. However, refinancing may incur fees or
    require additional credit checks.</p> 

    <p><u><b>17. Are there any restrictions on using the funds from a commercial bank loan?</u></b><br>
    • Answer: While loans are generally flexible, the bank may place restrictions on certain uses, such
    as excessive executive compensation or speculative investments. It’s essential to clarify with the
    bank what is allowed</p> 

    <p><u><b>18. What’s the difference between a commercial loan and an SBA loan?</u></b><br>
    • Answer: An SBA loan is partially backed by the U.S. Small Business Administration, making it
    less risky for banks to offer to smaller businesses. SBA loans often have lower interest rates and
    longer repayment terms but may require more paperwork and take longer to process.</p> 

    <p><u><b>19. Can I pay off the loan early?</u></b><br>
    • Answer: Many commercial loans allow for early repayment, but some may impose prepayment
    penalties. It’s important to check the loan agreement for terms related to early repayment.</p>

    <p><u><b>20. Is it possible to get a commercial loan with bad credit?</u></b><br>
    • Answer: It can be challenging to secure a loan with poor credit, but it’s not impossible. If your
    business has other strengths, such as solid revenue or assets, you may be able to negotiate better
    terms. Some banks may also offer loans specifically designed for businesses with lower credit
    scores but expect higher interest rates.</p>      
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def commercialbankingcommercialbankloantwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Commercial Bank Loans</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    The ideal stage for a company to use commercial bank loans is when it has moved past the
    startup phase, has a proven business model, and is in the growth or expansion stage with a steady
    revenue stream, positive cash flow, and a plan for using the loan effectively. At this stage, the
    company is likely to be in a good position to repay the loan and demonstrate to the bank that it
    can handle additional debt responsibly.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    The most ideal entity types for a business seeking commercial bank loans are corporations (C-
    Corp or S-Corp) and LLCs. These structures offer the necessary liability protection, financial
    reporting capabilities, and growth potential that make them attractive to banks. Banks tend to
    view corporations and LLCs as more stable and capable of managing larger loans and providing
    the necessary collateral and guarantees. However, this doesn’t mean that partnerships and sole
    proprietorships aren’t eligible.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    It is perfectly fine for businesses to have raised pre-capital before applying for a commercial
    bank loan. In fact, having raised pre-capital can be a positive factor when applying for a loan, as
    it indicates that your business has already gained the trust of investors or other lenders. However,
    it is essential to ensure that the business’s debt-to-equity ratio and repayment capacity remain
    within acceptable limits for the bank. A well-organized financial plan, a clear understanding of
    existing obligations, and a demonstrated ability to generate consistent cash flow are all key
    factors in successfully securing a commercial bank loan after raising pre-capital.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    While raising pre-capital is generally a positive factor that demonstrates investor confidence,
    there are specific restrictions or conditions associated with how that capital was raised that could
    interfere with securing a commercial bank loan. These include:
    <br>• High levels of existing debt.
    <br>• Investor rights or covenants that conflict with the bank’s interests.
    <br>• Ownership dilution that complicates decision-making.
    <br>• Lack of financial transparency or complex capital structures
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    The amount a company can raise using commercial bank loans depends on several factors,
    including the company’s financial health, creditworthiness, collateral, loan type, and the lender’s
    policies. Commercial banks generally offer a wide range of loan options, each with different
    borrowing limits. Small businesses might borrow anywhere from $50,000 to $5 million, but
    larger businesses or established corporations could secure loans for $10 million or more.
    </p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    The ideal capital round for a company that wants to use commercial bank loans is typically one
    where the business is in a growth or expansion phase, having secured enough initial capital to
    establish its operations and demonstrate its potential for generating stable cash flow, but not yet
    in need of substantial equity funding from venture capital or other investors. Specifically,
    companies that have successfully completed Seed or Series A rounds are often in a strong
    position to apply for commercial bank loans.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Yes, companies can use multiple tranches to raise capital through commercial bank loans,
    especially for large or complex financing needs. A multi-tranche loan structure allows businesses
    to borrow funds in stages, typically tied to specific milestones, needs, or conditions. This
    structure benefits both the lender (by managing risk) and the company (by offering flexibility
    and aligning funds with business growth). However, it’s essential to meet the milestones and
    conditions to ensure that each tranche is disbursed as planned.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    A business can use funds from commercial bank loans for various purposes, including covering
    working capital, capital expenditures, expansion, inventory purchases, acquisitions, or research
    and development. The specific loan type and how the funds are used will depend on the
    company’s immediate and long-term needs. These loans provide the flexibility to scale
    operations, manage cash flow, and invest in the future of the business<b>note(should be used from this list: {useoffund})</b></p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    A business needs to have moderate to high risk tolerance when taking out commercial bank
    loans. It must be comfortable with the risks of debt repayment, cash flow pressures, and potential
    loss of assets if the loan is secured. For startups or businesses in volatile industries, the tolerance
    for risk may be higher, as they may face greater uncertainty around profitability and cash flow.
    On the other hand, more established businesses may have a moderate risk tolerance, as they have
    the financial stability and track record to manage the regular payments and conditions that come
    with borrowing. Ultimately, the business must have solid financial planning, management
    capabilities, and a contingency strategy to successfully navigate the risks of taking on
    commercial bank loans.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    To successfully apply for commercial bank loans, a business should have a moderate to high
    capital cost tolerance. This involves the ability to manage interest payments, fees, loan
    repayments, and potentially fluctuating interest rates while ensuring that these costs do not
    impede business operations or profitability. Businesses should carefully assess the total cost of
    the loan, including both interest rates and fees, and choose the appropriate loan type based on
    their cash flow, growth projections, and financial stability. By understanding and planning for
    these costs, a business can ensure it is in a position to handle the obligations associated with
    commercial bank loans effectively.
    </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    <b>NOTE NEED A DYNAMIC RESPONSE!!!</b>On average, businesses can expect to spend between $1,000 and $15,000 in upfront costs for a
    commercial bank loan, depending on factors like the loan size, the type of loan, and the collateral
    requirements. Larger or more complex loans may incur additional costs. Understanding these
    costs and factoring them into the business's financial plan is essential before applying for a
    commercial bank loan.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    <b>NOTE NEED A DYNAMIC RESPONSE!!!</b>The time it takes for a business to secure a commercial bank loan generally ranges from 1 week
    to several weeks, depending on the type of loan, the business’s financial standing, the loan size,
    and the documentation required. Simple loans like business lines of credit can be processed
    within 1 to 2 weeks, while more complex loans (e.g., SBA loans, real estate loans) may take 3 to
    6 weeks or longer. The better prepared the business is with its documentation and financials, the
    quicker the process will be. Time to funding on larger and more complex loans can be around 8
    weeks.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)