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

def smallbusinessadministrationsbasbaveteran(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Small Business Administration (SBA)</b></u><br>
    Capital Type: SBA Veteran </center></p>
    <p><b><u>Introduction</u></b><br>
    The SBA Veteran financing programs are designed to support military veterans, service-disabled veterans, and their spouses in starting, purchasing, or expanding small businesses. {n} fits that definition. These programs are administered by the U.S. Small Business Administration and often provide favorable loan terms, fee reductions, and access to business development resources.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. SBA Veteran financing refers to loan programs supported by the U.S. Small Business Administration that are specifically targeted at veteran-owned businesses. These programs typically operate through SBA loan frameworks such as the 7(a) program and may include benefits such as reduced fees, counseling, and priority support. (U.S. Small Business Administration, n.d.)<br>
    <br>
    2. SBA Veteran loans are best suited for veteran-owned small businesses seeking startup capital, working capital, equipment financing, or expansion funding. (Investopedia, n.d.)<br>
    <br>
    3. Veteran-focused SBA financing programs were created to help military veterans transition successfully into entrepreneurship after service. (SBA Office of Veterans Business Development, n.d.)<br>
    <br>
    4. Although SBA Veteran loans offer favorable terms, they still require repayment and may involve strict qualification requirements. (U.S. Chamber of Commerce, 2023)<br>
    <br>
    5. To qualify for SBA Veteran financing, applicants must verify veteran status, operate a legally registered small business, and demonstrate a viable business plan. (Nav, 2024)
    </p>
    <p><u><b>References</b></u><br>
    U.S. Small Business Administration. (n.d.). Veteran-Owned Business Programs.<br>
    https://www.sba.gov/business-guide/grow-your-business/veteran-owned-businesses<br>
    SBA Office of Veterans Business Development. (n.d.).<br>
    https://www.sba.gov/offices/headquarters/ovbd<br>
    Investopedia. (n.d.). SBA Loans Overview.<br>
    https://www.investopedia.com/terms/s/small-business-administration.asp<br>
    U.S. Chamber of Commerce. (2023). Veteran Small Business Loans Guide.<br>
    https://www.uschamber.com/co/run/business-financing/veteran-small-business-loans<br>
    Nav. (2024). SBA Loans for Veterans.<br>
    https://www.nav.com/blog/sba-loans-for-veterans-25815 <br>
                             
    <p><u><b>Legal Qualification Requirements</u></b><br>
    Verified Veteran Status, Business must meet SBA small business size standards, Compliance with SBA loan eligibility requirements, Legally registered business entity, Personal and business credit evaluation, Demonstrated ability to repay the loan, Compliance with federal lending regulations, AML/KYC and identity verification
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    Proof of Veteran Status (DD-214 or equivalent documentation), Certificate of Business Registration, Business Plan, Financial Statements and Projections, Personal and Business Tax Returns, Credit History Reports, Loan Application Forms, Collateral Documentation (if required), Ownership and Cap Table Information
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def smallbusinessadministrationsbasbaveteranfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Small Business Administration (SBA)<br>
    SBA Veteran</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is the SBA Veteran program?</u></b><br>
    Answer: The SBA Veteran program is a set of initiatives offered by the U.S. Small Business Administration designed to support veteran-owned businesses through funding access, training, counseling, and federal contracting support.</p>
    <p><u><b>2. Who is eligible for SBA Veteran support?</u></b><br>
    Answer: Eligible participants typically include U.S. military veterans, active-duty service members transitioning to civilian life, National Guard and Reserve members, and military spouses.</p>
    <p><u><b>3. What types of businesses are best suited for SBA Veteran programs?</u></b><br>
    Answer: SBA Veteran programs support a wide range of small businesses across industries, including services, manufacturing, technology, retail, and government contracting.</p>
    <p><u><b>4. Do SBA Veteran programs provide direct funding?</u></b><br>
    Answer: SBA Veteran programs do not usually provide direct grants. Instead, they facilitate access to SBA-backed loans, loan guarantees, and specialized financing programs.</p>
    <p><u><b>5. How much funding can a business access?</u></b><br>
    Answer: Funding amounts depend on the SBA loan program used. Loan sizes can range from small microloans to larger loans for expansion.</p>
    <p><u><b>6. How quickly can funding be accessed?</u></b><br>
    Answer: The process typically takes several weeks to months, depending on documentation and business readiness.</p>
    <p><u><b>7. Do SBA Veteran programs require equity dilution?</u></b><br>
    Answer: No. SBA Veteran programs are debt-based support mechanisms. Business owners retain full ownership and control.</p>
    <p><u><b>8. Can SBA Veteran support be combined with other funding sources?</u></b><br>
    Answer: Yes. SBA Veteran programs can be combined with personal savings, angel investment, accelerators, or other programs.</p>
    <p><u><b>9. What non-financial support do SBA Veteran programs provide?</u></b><br>
    Answer: Programs offer entrepreneurship training, counseling, mentorship, business planning assistance, and access to VBOCs.</p>
    <p><u><b>10. What is the role of VBOCs?</u></b><br>
    Answer: VBOCs provide targeted training, counseling, and mentoring to veteran entrepreneurs.</p>
    <p><u><b>11. Do SBA Veteran programs help with government contracting?</u></b><br>
    Answer: Yes. SBA Veteran programs assist eligible businesses in accessing federal contracting opportunities.</p>
    <p><u><b>12. What are the key benefits?</u></b><br>
    Answer: Key benefits include improved access to capital, no equity dilution, government-backed loan guarantees, and specialized training.</p>
    <p><u><b>13. What are the risks or limitations?</u></b><br>
    Answer: Risks include loan repayment obligations, personal guarantees, and longer approval timelines.</p>
    <p><u><b>14. How does SBA Veteran support compare to private investors?</u></b><br>
    Answer: SBA Veteran programs focus on stability and ownership retention, while private investors prioritize rapid growth and returns.</p>
    <p><u><b>15. How can veterans improve their chances?</u></b><br>
    Answer: Veterans should prepare a strong business plan, maintain good credit, leverage VBOC counseling, and demonstrate repayment ability.</p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def smallbusinessadministrationsbasbaveterantwelve(request):
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
    Capital Type: SBA Veteran</p></center>
    <p><b><u>1 - Stage of Development Assessment</u></b><br>
    SBA Veteran programs are best suited for early-stage to established small businesses, including startups with a clear business plan and operating businesses seeking growth, stabilization, or expansion.</p>
    <p><b><u>2 - Entity Type Assessment</u></b><br>
    SBA Veteran programs are available to most formal business entities, including sole proprietorships, partnerships, LLCs, and corporations. The key requirement is that the business must be majority-owned (at least 51%) and controlled by a veteran.</p>
    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    Applicants are expected to demonstrate owner equity investment and commitment before accessing SBA-backed financing.</p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    SBA Veteran programs are not equity-based and do not operate in venture capital markets.</p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    SBA Veteran loans can support moderate to large capital needs, depending on the loan program.</p>
    <p><b><u>6 - Capital Round Assessment</u></b><br>
    SBA Veteran funding does not follow traditional startup funding rounds. Instead, it aligns with operational financing stages.</p>
    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    Funds are typically disbursed in a single lump sum upon loan approval and closing.</p>
    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    Approved uses include working capital, equipment and machinery, inventory purchase, business acquisition, commercial real estate, and refinancing certain existing business debts.</p>
    <p><b><u>9 - Risk Assessment</u></b><br>
    The risk level is moderate. While SBA guarantees reduce lender risk, the borrower remains fully responsible for repayment.</p>
    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    The cost of capital is moderate, consisting of interest rates and SBA guarantee fees.</p>
    <p><b><u>11 - Upfront Cost Assessment</u></b><br>
    Upfront costs may include loan packaging fees, legal fees, appraisal costs, and closing expenses.</p>
    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
    The timeline to capital is moderate, typically ranging from 30 to 90 days.</p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
