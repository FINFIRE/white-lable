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

def smallbusinessadministrationsbasba7a(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Small Business Administration (SBA)</b></u><br>
    Capital Type: SBA 7A </center></p>
    <p><b><u>Introduction</u></b><br>
    The SBA 7(a) Loan is ideal for companies seeking versatile financing for a wide range of business purposes, including working capital, expansion, equipment purchases, and debt refinancing. It is designed so that government-guaranteed loans from private lenders can help privately held startups and small businesses access capital that might otherwise be unavailable through conventional channels. {n} fits that definition. The 7(a) program is the SBA's primary and most popular lending vehicle. In Fiscal Year 2024, the program provided over $31 billion in funding to small businesses across the United States. Because the SBA guarantees up to 85% of the loan amount for the lender, it encourages banks to offer more favorable terms and longer repayment periods to entrepreneurs. On average, 7(a) loan recipients gain access to between $50,000 and $5 million, with repayment terms extending up to 10 years for working capital and 25 years for real estate. While the 7(a) loan is highly flexible, the requirement for personal guarantees from all major owners, strict eligibility criteria regarding "size standards," and the detailed documentation required for the federal guarantee process can make the application timeline more intensive than traditional bank products.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. The SBA 7(a) Loan is a government-guaranteed loan program where the SBA does not lend money directly to the business. Instead, it provides a guarantee to a private lender (bank or credit union) that it will repay a portion of the loan if the borrower defaults. This "credit enhancement" allows lenders to provide financing to businesses that may have "weaknesses" in their collateral or credit history but otherwise demonstrate a strong ability to repay. (SBA.gov, 2025)<br>
    <br>
    2. The best type of companies to raise money via the 7(a) program are for-profit small businesses that operate in the United States, have reasonable owner equity to invest, and have exhausted other financial resources. It is particularly effective for startups with strong business plans, service-based businesses with few physical assets (low collateral), and companies looking to acquire an existing business or franchise. (Forbes Advisor, 2025)<br>
    <br>
    3. The 7(a) program emerged from the Small Business Act of 1953, which established the SBA to "aid, counsel, assist and protect" small business interests. Over the decades, it has evolved into a global model for credit guarantees. In 2025, the program continues to adapt through the "SBA Express" and "Community Advantage" sub-programs, which target faster approvals for smaller amounts and increased lending in underserved and rural communities. (Congressional Research Service, 2024)<br>
    <br>
    4. While 7(a) loans offer favorable terms, there are inherent risks and costs. Borrowers are typically required to pay an "SBA Guaranty Fee," which is based on the loan amount and maturity; this fee can be several thousand dollars, though it can usually be financed into the loan. Additionally, lenders are required to take as much collateral as available (up to the loan amount). If the business fails, the SBA's guarantee protects the bank, not the borrower, meaning the owner remains personally liable for the full debt. (Lendio, 2025)<br>
    <br>
    5. To raise capital via an SBA 7(a) loan, a founder must apply through an SBA-approved lender. The process includes a thorough evaluation of the "Five Cs of Credit," with a heavy emphasis on the "Capacity" of the business to generate enough cash flow to cover debt payments. Many lenders participate in the "Preferred Lender Program" (PLP), which allows them to make final credit decisions without sending the application to the SBA for a separate review, significantly shortening the approval time. (SmartBiz, 2025)
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Small Business Size – Must meet SBA size standards (typically based on industry-specific revenue or employee count).<br>
    · For-Profit Status – The business must be for-profit; non-profits are ineligible for 7(a) funding.<br>
    · U.S. Based – Must be physically located and operating within the United States or its territories.<br>
    · Personal Guarantee – All individuals with a 20% or greater ownership stake must provide a personal guarantee.<br>
    · Owner Equity – Startups typically require a cash injection of at least 10% to 20% of the total project cost.<br>
    · Eligible Purpose – Funds cannot be used for passive investment, gambling, or pyramid schemes.<br>
    · No Delinquent Federal Debt – Neither the business nor the owners can be delinquent on federal loans (e.g., student loans, taxes).<br>
    · Demonstrated Need – The borrower must show that they cannot obtain the same terms from a non-SBA-backed loan.
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    · SBA Form 1919 – Borrower Information Form.<br>
    · Personal Financial Statement (SBA Form 413) – Required for all owners with 20% or more interest.<br>
    · Business Tax Returns – Federal filings for the last 3 years.<br>
    · Personal Tax Returns – Federal filings for the last 3 years for all major owners.<br>
    · Business License/Registration – Proof of legal entity and authorization to operate.<br>
    · Profit & Loss (P&L) Statement – Current within the last 90–120 days.<br>
    · Balance Sheet – Current within the last 90–120 days.<br>
    · Business Debt Schedule – List of all current installment loans, leases, and notes payable.<br>
    · Resumes of Key Personnel – Demonstrating management experience.<br>
    · Business Overview/History – A brief narrative explaining the company and why the loan is needed.
    </p>
    <p><u><b>References</b></u><br>
    SBA.gov. (2025, March 12). 7(a) Loans: Our most common loan program. https://www.sba.gov/funding-programs/loans/7a-loans<br>
    Forbes Advisor. (2025, January 10). SBA 7(a) Loan: Everything You Need To Know. https://www.forbes.com/advisor/business-loans/sba-7a-loan/<br>
    Congressional Research Service (CRS). (2024, May 08). Small Business Administration 7(a) Loan Guaranty Program. https://crsreports.congress.gov/product/pdf/R/R41146<br>
    Lendio. (2025). Pros and Cons of SBA 7(a) Loans. https://www.lendio.com/sba-loans/7a-loan-guide/<br>
    SmartBiz. (2025). How to Apply for an SBA 7(a) Loan. https://www.smartbizloans.com/sba-7a-loan-application
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def smallbusinessadministrationsbasba7afaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Small Business Administration (SBA)<br>
    SBA 7A</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is the SBA 7(a) loan, and how does it differ from other SBA programs?</u></b><br>
    • Answer: The SBA 7(a) loan is the SBA's most flexible financing program, providing funding for working capital, expansion, equipment, refinancing, and acquisitions, unlike asset-specific programs such as SBA 504.
    </p>
    <p><u><b>2. What types of businesses are best suited for SBA 7(a) loans?</u></b><br>
    • Answer: Small businesses across most industries, including startups and growing companies needing flexible capital, are well-suited for SBA 7(a) financing.
    </p>
    <p><u><b>3. How much funding can I receive through an SBA 7(a) loan?</u></b><br>
    • Answer: SBA 7(a) loans offer funding of up to $5 million, depending on business size, cash flow, and lender criteria.
    </p>
    <p><u><b>4. How quickly can I access funds through an SBA 7(a) loan?</u></b><br>
    • Answer: Funding typically takes 30 to 90 days, with SBA Express options offering faster approval timelines.
    </p>
    <p><u><b>5. What are the costs associated with SBA 7(a) loans?</u></b><br>
    • Answer: Costs include interest rates, SBA guaranty fees, lender fees, and closing costs, though rates are generally competitive compared to traditional bank loans.
    </p>
    <p><u><b>6. Do I have to give up equity to receive an SBA 7(a) loan?</u></b><br>
    • Answer: No, SBA 7(a) loans are debt financing, allowing business owners to retain full ownership.
    </p>
    <p><u><b>7. Can SBA 7(a) funds be used for multiple business purposes?</u></b><br>
    • Answer: Yes, funds can be used for working capital, inventory, equipment, real estate, refinancing debt, or business acquisition.
    </p>
    <p><u><b>8. What are the main benefits of SBA 7(a) loans?</u></b><br>
    • Answer: Benefits include flexible use of funds, longer repayment terms, lower down payments, and SBA-backed risk reduction for lenders.
    </p>
    <p><u><b>9. What collateral is required for SBA 7(a) loans?</u></b><br>
    • Answer: Collateral is required when available and may include business assets, real estate, and personal guarantees from owners.
    </p>
    <p><u><b>10. What happens if I default on an SBA 7(a) loan?</u></b><br>
    • Answer: Default may result in collection actions, asset liquidation, and enforcement of personal guarantees, even though the SBA guarantees part of the loan.
    </p>
    <p><u><b>11. Are there risks associated with SBA 7(a) loans?</u></b><br>
    • Answer: Risks include long approval processes, strict documentation requirements, and personal liability for repayment.
    </p>
    <p><u><b>12. How does SBA 7(a) compare to conventional business loans?</u></b><br>
    • Answer: SBA 7(a) loans typically offer more favorable terms and lower down payments, while conventional loans may have faster approvals but stricter credit requirements.
    </p>
    <p><u><b>13. Can startups qualify for SBA 7(a) loans?</u></b><br>
    • Answer: Yes, startups may qualify if they demonstrate strong business plans, management experience, and sufficient cash flow projections.
    </p>
    <p><u><b>14. What types of businesses typically benefit most from SBA 7(a) financing?</u></b><br>
    • Answer: Retail, service-based, professional, and growth-stage businesses benefit most due to the program's flexibility.
    </p>
    <p><u><b>15. How can I increase my chances of SBA 7(a) loan approval?</u></b><br>
    • Answer: Improve credit scores, prepare detailed financial projections, demonstrate repayment ability, and work with SBA-approved lenders.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def smallbusinessadministrationsbasba7atwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Small Business Administration (SBA)</b></u><br>
    Capital Type: SBA 7A</p></center>
    <p><b><u>1 - Stage of Development Assessment</u></b><br>
    SBA 7(a) loans are best suited for established small businesses and early-growth companies with operating history. Startups may qualify, but lenders typically prefer businesses with cash flow, revenue, and management experience.
    </p>
    <p><b><u>2 - Entity Type Assessment</u></b><br>
    Eligible entity types include C-Corps, LLCs, S-Corps, partnerships, and sole proprietorships. The business must be for-profit and operating in the U.S. (or qualifying territory).
    </p>
    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    Businesses are expected to demonstrate adequate owner investment, reasonable creditworthiness, and the inability to obtain conventional financing without SBA support. Existing debt and capital structure are closely reviewed.
    </p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    SBA 7(a) loans operate through commercial banks and SBA-approved lenders, supported by a government guarantee. Prior equity or debt financing does not disqualify a business but impacts lender risk assessment.
    </p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    SBA 7(a) loans can fund up to $5 million, depending on business size, cash flow, and purpose of funds. This makes it suitable for moderate to large capital needs.
    </p>
    <p><b><u>6 - Capital Round Assessment</u></b><br>
    This financing does not align with equity funding rounds. It is typically used as growth-stage debt capital, either as a standalone loan or alongside owner equity.
    </p>
    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    Funds are generally disbursed in a single tranche at closing, though construction or phased projects may involve multiple disbursements.
    </p>
    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    Permitted uses include:<br>
    · Working capital<br>
    · Equipment purchases<br>
    · Business acquisition<br>
    · Real estate acquisition or improvement<br>
    · Debt refinancing<br>
    Restrictions apply to speculative activities, investment properties, and personal use.
    </p>
    <p><b><u>9 - Risk Assessment</u></b><br>
    Risk is moderate, as loans are partially guaranteed by the SBA. However, owners are typically required to provide personal guarantees, and default can impact personal credit and assets.
    </p>
    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    Costs include interest rates (variable or fixed), SBA guarantee fees, and bank fees. While generally lower than unsecured loans, repayment obligations create long-term financial commitments.
    </p>
    <p><b><u>11 - Up Front Cost Assessment</u></b><br>
    Upfront costs may include SBA guarantee fees, legal fees, appraisal costs, and lender origination fees, typically ranging from moderate to high depending on loan size.
    </p>
    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
    The approval and funding process usually takes 30 to 90 days, depending on lender efficiency, documentation readiness, and SBA review requirements.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
