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


def smallbusinessadministrationveteran(request):
    introduction = mark_safe("""
    <p><center><b><u>Capital Market: Small Business Administration</b></u><br>
    Capital Type: Veteran Loan</center></p>
    <p><b><u>Introduction</u></b><br>
    Fiscal year 2024 marked a notable rise in SBA-backed loans, with more than 3,100 loans issued
    to veteran-owned small businesses, totaling $1.3 billion. Total loans are up almost 48% under the
    Biden-Harris Administration, and total loan dollars are up 51%. <a href="https://www.fsuvboc.com/Blog/Celebrating-2024-VetBiz-Achievements-and-Growth">This progress illustrates the
    SBA’s dedication to helping veteran entrepreneurs access essential funding, ensuring they have
    the resources needed to launch and grow their businesses.</a></p>

    <p><b><u>Definition of Capital Type</b></u><br> 
    1) The SBA Veterans Advantage program is a loan type under the SBA 7(a) loan program. It’s
    intended for small businesses that are majority-owned (meaning 51% or more) by veterans,
    active duty service members or military spouses or widows. As with any SBA 7(a) loan, loans
    can be up to $5 million with repayment terms around 10 years or 25 years for real estate loans.
    Most loans under the Veterans Advantage program average $350,000, but your loan amount will
    depend on what you need the funds for and what type of business you run. (Cox, 2024)</p>
                             
    <p>2) The Small Business Administration has a program in place designed to assist veterans of the
    U.S. armed forces in acquiring capital to start, grow, or succeed in their business endeavors. The
    Veterans Advantage Program was established to support veterans, who play a large role in
    stimulating economic growth in local communities. In an effort to encourage lending to veterans
    with small businesses, the SBA provides reductions for some loan program fees.</p>
                             
    <p>In addition to the reduced fees, the small business administration offers counseling and online
    training courses aimed at making veterans lender ready. The SBA does this in line with its
    singular goal of reducing barriers for veteran business owners so that they may have access to
    more capital and create more jobs. The Veterans Advantage Program extends to any business that
    is at least 51% owned and controlled by an individual or individuals who meet the following
    criteria:<br>
    • Honorably Discharged Veteran(s)
    <br>• Active Reservist and/or Active National Guard Member
    <br>• Active Duty Military service members who qualify for the Transition Assistance Program
    <br>• Current Spouse of any veteran, active duty service member, reservist, or national guard
    member
    <br>• Widowed spouse of a service member who died while in service, or as a result of a
    service-related disability (What Is the SBA Veterans Advantage Program?, 2023).</p>

    <p>3) SBA loan rates for veterans under the Veterans Advantage program are generally more
    favorable than standard SBA loan rates. These favorable terms are part of the SBA's commitment
    to supporting veterans in their entrepreneurial ventures.</p>
                             
    <p>One of the significant benefits is the reduction or waiver of the upfront loan guarantee fees,
    making these loans more affordable for veterans.</p>
                             
    <p>The interest rates for SBA Veterans Advantage 7(a) loans are typically competitive, offering
    veterans an affordable financing option. The exact rate can vary based on the loan amount, term,
    and current market rates.</p>
                             
    <p>The SBA Veterans Advantage 7(a) program offers a tangible way for veterans to secure loans and
    build their businesses, with tailored requirements, a straightforward application process, and
    favorable loan rates. (Taylor, 2024)</p>
    
    <p><b><u>References</b></u><br>
    Cox, K. (2024, August 12). SBA loan rates for veterans. Retrieved from Swoop Funding:
    <a href="https://swoopfunding.com/us/sba-loans/sba-loans-for-veterans/veterans-rates/">https://swoopfunding.com/us/sba-loans/sba-loans-for-veterans/veterans-rates/</a></p>
                             
    <p>Taylor, M. (2024, February 16). Empowering Veteran Entrepreneurs. Retrieved from Rok
    Financial: <a href="https://www.rok.biz/blog/empowering-veteran-entrepreneurs-a-guide-to-sba-
    veterans-advantage-7a-loans">https://www.rok.biz/blog/empowering-veteran-entrepreneurs-a-guide-to-sba-
    veterans-advantage-7a-loans/</a></p>
                             
    <p>What Is the SBA Veterans Advantage Program? (2023, October 5). Retrieved from Janover:
    <a href="https://www.sba7a.loans/sba-7a-loans-small-business-blog/sba-veterans-advantage-
    program">https://www.sba7a.loans/sba-7a-loans-small-business-blog/sba-veterans-advantage-
    program/</a>
    </p>
                             
    <p><u><b>Legal Qualification Requirements</u></b>
    <br>• To qualify, the business must be 51% owned and controlled by:
    <br>&emsp;- Veterans
    <br>&emsp;-Active-duty military members, including those in the Transition Assistance Program
    <br>&emsp;-Reservists or members of the National Guard
    <br>&emsp;-Spouse of anyone of the above, including widows
    <br>• Be an operating, for profit business located in the U.S.
    <br><a href="https://www.ecfr.gov/current/title-13/chapter-I/part-121">• Be small under SBA Size Requirements</a>
    <br><a href="https://www.ecfr.gov/current/title-13/chapter-I/part-120/subpart-A/subject-group-ECFR6d9c2c4fd6e44c1/section-120.11">• Not be a type of ineligible business</a>
    <br>• Be creditworthy and demonstrate a reasonable ability to repay the loan
    <br>• Credit Score: Although the SBA itself doesn’t set an official minimum credit score, most
    lenders require a credit score of 650 or higher. In some cases, depending on the loan size and
    lender, a score as high as 680 or 700 may be necessary.
    <br>• Good Character: Borrowers must pass a background check, and a criminal history—
    particularly financial-related offenses—may affect eligibility.
    <br>• Demonstrated Need for Credit: Applicants must demonstrate they cannot secure credit
    from other sources on reasonable terms, documenting previous loan attempts and rejections.
    <br>• Business Plan: A clear and feasible business plan is essential for showing how the loan
    will support business operations and growth.
    <br>• No Government Debt: Borrowers must not be delinquent on any federal loans, such as
    existing SBA loans or federal tax debts.</p>
    
    <p><b><u>Supporting Document List</u></b>
    <br>• SBA Form 1919: Borrower Information Form (required for all applicants).
    <br>• SBA Form 912: Statement of Personal History (required for principal owners).
    <br>• SBA Form 413: Personal Financial Statement.
    <br>• DD Form 214 required for any veteran or military spouse
    <br>• DD Form 2 required for Reservists, National Guard members, and transitioning out of
    active duty
    <br>• DD Form 1173 required for spouses of transitioning military service members
    <br>• Legal business registration documents (e.g., articles of incorporation)
    <br>• Lease agreements (if applicable)
    <br>• Financial statements for the last three years (including income statements, balance sheets,
    and cash flow statements)
    <br>• Three years of business and personal tax returns
    <br>• Current profit & loss (P&L) statements and balance sheets
    <br>• Details of present debt obligations
    <br>• A detailed schedule of any collateral you are offering
    <br>• Resumes for all business owners.</p>                                                                           
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def smallbusinessadministrationveteranfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Small Business Administration<br>
    Capital Type: Veteran Loan</center></p>                        
    <p><center><u><b>Frequently Asked Question for Veteran Loan</u></b></center></p>
                             
    <p><u><b>1. What is an SBA Veterans Advantage Loan?</u></b><br>
    •Answer:The SBA Veterans Advantage Loan is a specific SBA 7(a) loan program that
    provides favorable terms to veteran-owned small businesses. It offers lower guarantee
    fees and other financial incentives to veterans and their spouses who own and operate
    small businesses.</p>
                             
    <p><u><b>2. How is the SBA Veterans Advantage Loan different from other SBA loans?</u></b><br>
    • Answer: Unlike standard SBA loans, the Veterans Advantage program offers reduced
    guarantee fees (as much as 50% lower) for veterans, reservists, and active-duty military
    personnel. This makes it a more affordable borrowing option compared to other SBA
    programs.</p>
                             
    <p><u><b>3. Who qualifies for the SBA Veterans Advantage Loan?</u></b><br>
    • Answer: To qualify, the business must be at least 51% veteran-owned or majority-owned
    by active-duty military personnel, veterans, or their spouses. Additionally, the business
    must meet the general SBA 7(a) eligibility requirements, including the size standard and
    creditworthiness criteria.</p>
                             
    <p><u><b>4. What types of businesses are eligible for an SBA Veterans Advantage Loan?</u></b><br>
    • Answer: The SBA Veterans Advantage Loan can be used by businesses in nearly all
    industries, including retail, service, manufacturing, and more, as long as they meet SBA
    size requirements and are veteran-owned.</p>
                             
    <p><u><b>5. What can the SBA Veterans Advantage Loan be used for?</u></b><br>
    • Answer:he loan can be used for a wide variety of business purposes, including:
    <br>• Working capital
    <br>• Equipment purchase
    <br>• Debt refinancing
    <br>• Real estate (e.g., buying or improving property)
    <br>• Inventory purchases
    <br>• Business expansion</p>
                             
    <p><u><b>6. What are the interest rates for the SBA Veterans Advantage Loan?</u></b><br>
    • Answer: Interest rates are determined by the SBA and can vary based on the size of the
    loan and repayment terms. Typically, they are lower than conventional loans, and the
    rates range from 7.5% to 9%, depending on the loan amount.</p>
                             
    <p><u><b>7. What are the key benefits of choosing an SBA Veterans Advantage Loan?</u></b><br>
    • Answer: Some key benefits include:
    <br>• Lower SBA guarantee fees (up to 50% lower for veterans)
    <br>• Longer repayment terms (up to 10 years for working capital and 25 years for real estate)
    <br>• Competitive interest rates
    <br>• Easier qualification for veterans with a strong credit profile
    </p>
                             
    <p><u><b>8. How much can I borrow with an SBA Veterans Advantage Loan?</u></b><br>
    • Answer: The SBA Veterans Advantage Loan program offers loans up to $5 million.</p>
                             
    <p><u><b>9. What are the repayment terms for an SBA Veterans Advantage Loan?</u></b><br>
    • Answer: Repayment terms generally range from 5 to 10 years for working capital and up
    to 25 years for real estate purchases. Repayment terms are typically longer than
    conventional loans, which can be beneficial for businesses needing more time to repay.
    </p>
                             
    <p><u><b>10. How long does it take to get approved for an SBA Veterans Advantage Loan?</u></b><br>
    • Answer:he approval process typically takes 30 to 60 days, depending on the lender, the
    size of the loan, and the complexity of the business’s financials. Preferred Lenders may
    offer a quicker turnaround.
    </p>
                             
    <p><u><b>11. What is the maximum amount I can raise using Rule 506(c)?</u></b><br>
    • Answer: Yes, there are guarantee fees after $150,000 and possible lender fees. The
    guarantee fees are lower for veterans than for non-veteran applicants. Lender fees can
    include application, processing, and closing fees, but they are typically lower than those
    charged by traditional lenders.
    </p>
                             
    <p><u><b>12. Can I use the SBA Veterans Advantage Loan to refinance existing debt?</u></b><br>
    • Answer: Yes, refinancing existing debt is one of the permitted uses of the loan. This could
    help businesses reduce interest costs or consolidate loans into one manageable
    repayment.
    </p>
                             
    <p><u><b>13. Do I need to provide collateral for an SBA Veterans Advantage Loan?</u></b><br>
    • Answer:Yes, the SBA typically requires collateral for loans over $25,000. This can
    include business assets, real estate, or personal assets if necessary. However, the SBA
    does not require personal guarantees for loans under $200,000 if the business owner’s
    credit is strong.
    </p>
                             
    <p><u><b>14. How is the SBA Veterans Advantage Loan different from other types of business loans?</u></b><br>
    • Answer: Compared to traditional business loans or even other SBA loan programs, the
    Veterans Advantage provides lower fees and better terms for veteran business owners.
    Additionally, veterans may have access to special programs and support tailored to their
    needs, such as priority processing and mentoring opportunities</p> 
                             
    <p><u><b>15. What documents do I need to apply for an SBA Veterans Advantage Loan?</u></b><br>
    • Answer:Key documents include:
    <br>• Proof of veteran status (e.g., DD-214 form or VA disability letter)
    <br>• Personal and business tax returns (typically for the past 2-3 years)
    <br>• Business financial statements (balance sheets, profit and loss statements)
    <br>• Business plan (including use of funds, market analysis, and growth projections)
    <br>• Personal financial statement (if the owner is required to provide a personal guarantee)
    </p>
                             
    <p><u><b>16. What happens if my business does not qualify for an SBA Veterans Advantage Loan?</u></b><br>
    • Answer:f your business does not qualify for the Veterans Advantage Loan, you may still
    be eligible for a standard SBA 7(a) loan or other forms of alternative financing (e.g.,
    traditional loans, lines of credit, or private investment).
    </p>

    <p><u><b>17. Can I apply for an SBA Veterans Advantage Loan if I already have other SBA loans or
    funding?</u></b><br>
    • Answer:Yes, as long as your business meets the eligibility requirements and can
    demonstrate the ability to manage additional debt. However, if you already have
    significant debt obligations, it may affect your ability to qualify for a new SBA loan.
    </p>
                             
    <p><u><b>18. Can I use the SBA Veterans Advantage Loan for a startup business?</u></b><br>
    • Answer:While the SBA Veterans Advantage Loan is not specifically designed for
    startups, it is possible for new businesses to qualify if they have a solid business plan and
    good personal credit. Lenders may require additional documentation or collateral for
    startups.
    </p>

    <p><u><b>19. How do I find lenders that offer SBA Veterans Advantage Loans?</u></b><br>
    • Answer:he SBA has a network of Preferred Lenders who are authorized to process SBA
    loans. You can find participating lenders through the SBA’s website, or you can directly
    inquire with your bank to see if they offer the Veterans Advantage program.
    </p>                                                                                                                                                                                                       
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def smallbusinessadministrationveterantwelve(request):
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
    SBA Veteran Loans</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    The ideal stage for using the SBA Veterans Advantage loan is typically at the early stage or
    growth stage, where you are either starting a new business or looking to expand an existing one.
    Having a solid business plan, financial stability, and a clear path for growth will make it easier to
    qualify for and effectively use this loan.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    The most ideal entity types for applying for an SBA Veterans Advantage Loan are:
    &emsp;<br>• Limited Liability Company (LLC) – Provides flexibility, limited liability protection, and
    is relatively simple to set up and maintain.
    &emsp;<br>• S Corporation (S Corp) – Good for small businesses that want the pass-through taxation
    benefits and are prepared to meet corporate formalities.
    &emsp;<br>• C Corporation (C Corp) – Suitable for larger or more complex businesses looking to scale
    rapidly, though less ideal for small startups.
    <br>While a sole proprietorship or partnership may be eligible, these structures are less favorable due
    to limited liability protection and potential challenges in financing and taxation.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    It is perfectly acceptable for a business to have raised pre-capital before applying for an SBA
    Veterans Advantage Loan. In fact, it can be a sign of preparedness and financial stability, which
    can improve your chances of securing the loan. Just ensure that the raised capital is properly
    documented, used for legitimate business purposes, and that you demonstrate your ability to
    repay the loan.  
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    Raising pre-capital before applying for the SBA Veterans Advantage Loan is generally fine, but
    you must ensure that the business maintains 51% veteran ownership if any equity has been
    diluted through capitalization.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    The SBA Veterans Advantage loan can lend up to $5 million for qualified businesses.
    </p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    The ideal capital round for a company that wants to use the SBA Veterans Advantage Loan
    typically falls within the early to growth stage, often during a seed or Series A stage, or after
    securing pre-seed capital. This is when a business is in its startup or growth phase and seeking
    additional funding to expand operations, purchase assets, or cover working capital needs.</p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    You cannot use more than one tranche within a single SBA Veterans Advantage Loan, as it’s a
    single loan that is approved and disbursed as one lump sum. However, you can use the funds in
    different stages of business growth as long as they align with the purpose outlined in the loan
    application. If you require additional capital, you may need to apply for other SBA loans or use
    other funding sources after securing the initial loan.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    The SBA Veterans Advantage Loan provides a flexible financing option that can be used for a
    wide range of business purposes, including working capital, equipment purchases, debt
    refinancing, expansion, marketing, and facility improvements, among others. The key is that the
    funds must be used for business-related activities that help grow and sustain the business. Be
    sure to outline the intended use of funds clearly in your application to ensure compliance with
    SBA requirements.</p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    For a business to successfully use an SBA Veterans Advantage Loan, it should have moderate to
    low risk tolerance. This includes a willingness to manage debt responsibly, take on financial
    obligations with the understanding that repayment is required, and plan for both the opportunities
    and potential challenges that come with borrowing.<br>
    A business with a stable cash flow, a solid repayment plan, and strategic long-term growth plans
    is best suited for an SBA loan, while businesses that are risk-averse or struggling with financial
    stability may face challenges in qualifying or maintaining repayment terms.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    A business seeking an SBA Veterans Advantage Loan should have a moderate capital cost
    tolerance—meaning that it can comfortably manage the ongoing costs of the loan (interest, fees,
    and principal repayment) while ensuring the loan is used to generate growth and increase cash
    flow.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    The upfront costs for an SBA Veterans Advantage Loan typically range from $4,000 to $10,000
    for smaller loans (under $150,000) and can be up to or higher that $15,000 for larger loans, with
    fees being mainly made up of the SBA guarantee fee, lender fees, application fees, and any third-
    party services. It's important for businesses to budget for these costs and ensure they have
    sufficient capital available to cover them in addition to the loan amount.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    On average, a business can expect to receive an SBA Veterans Advantage Loan within 30 to 60
    days, depending on the lender, loan size, and the completeness of the application. Smaller loans
    typically take less time, while larger loans or those requiring further SBA review may take
    longer. To speed up the process, ensure that all required documentation is complete and accurate,
    and communicate promptly with the lender if additional information is requested.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)