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

def smallbusinessadministrationsbacdcsbdc(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Small Business Administration (SBA)</b></u><br>
    Capital Type: CDC/SBDC </center></p>
    <p><b><u>Introduction</u></b><br>
    The SBA ecosystem provides two distinct but complementary "resource partner" paths: Certified Development Companies (CDCs) and Small Business Development Centers (SBDCs). CDCs are ideal for companies seeking long-term, fixed-asset financing (the 504 Loan), while SBDCs are designed so that entrepreneurs can receive free professional counseling and technical assistance to prepare for such capital. {n} fits the definition of a business that may utilize these for growth. The CDC/SBDC infrastructure is a cornerstone of American small business development. In 2025, the SBDC network comprises over 1,000 centers nationwide, providing roughly 1.2 million hours of counseling annually. Concurrently, CDCs—of which there are approximately 200—facilitate the SBA 504 program, which hit a milestone of over $9 billion in funding in 2024. While SBDCs do not provide money directly, they serve as the "pre-capital" engine that helps businesses become "bankable" for CDC-led loans. While this system offers a "Window to Wall Street" (CDC) and "Elite Consulting for Free" (SBDC), the primary risk is the complexity of the 504 loan structure and the potential for long wait times at busy SBDC regional offices.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. Certified Development Companies (CDCs) are specialized non-profit corporations certified and regulated by the SBA. Their primary role is to package, process, and service SBA 504 loans. They work in a 50/40/10 partnership with private banks to provide fixed-rate financing for major assets like real estate or heavy machinery. (SBA.gov, 2025)<br>
    <br>
    2. Small Business Development Centers (SBDCs) are a partnership between the SBA and universities or state agencies. Unlike CDCs, they are non-lending entities. Their "capital value" lies in technical assistance: helping founders draft business plans, financial projections, and loan application packages that increase the likelihood of approval from CDCs or banks. (OCC.gov, 2025)<br>
    <br>
    3. The CDC program emerged from the Small Business Investment Act of 1958, while the SBDC program was authorized in 1980. Together, they represent a shift toward decentralized economic development. By the mid-2020s, these programs have evolved to include specialized focuses on "Community Advantage" lending and technology transfer, ensuring that underserved and high-tech markets have access to both capital and "know-how." (America's SBDC, 2025)<br>
    <br>
    4. While CDCs provide low-down-payment loans, they carry strict "public policy" requirements. For a CDC to fund a project, the business must typically meet a job creation goal (e.g., creating 1 job for every $75,000–$95,000 borrowed). If the business is purely for investment or speculation (like a passive rental property), it is legally ineligible for CDC/504 funding. (OCC.gov, 2025)<br>
    <br>
    5. To leverage this market, a founder should start at an SBDC to refine their financials for free. Once "loan-ready," the SBDC often introduces the founder to a CDC, which then coordinates with a traditional bank. This "warm handoff" significantly reduces the administrative friction of the 504 loan application, which can otherwise take 60–90 days to close. (Capital CDC, 2025)
    </p>
    <p><u><b>Legal Qualification Requirements (CDC/504)</u></b><br>
    · Size Standards – Tangible net worth must be <$20M and average net income <$6.5M.<br>
    · For-Profit Status – Non-profit entities are ineligible for 504 loans (though CDCs themselves are non-profits).<br>
    · Owner-Occupancy – Business must occupy at least 51% of an existing building or 60% of new construction.<br>
    · Job Creation – Must create/retain one job per $75k–$95k of the debenture (with exceptions for public policy goals).<br>
    · Personal Guarantee – Required for all owners with 20% or more stake.<br>
    · No Credit Elsewhere – Must show that the loan is not available on similar terms without the SBA guarantee.<br>
    · Character Eligibility – No "bad actor" events, pending criminal charges, or defaults on prior federal debt.
    </p>
    <p><u><b>Supporting Document List (SBDC Prep for CDC)</u></b><br>
    · Business Plan – A comprehensive document (SBDCs can help write this for free).<br>
    · Financial Projections – 24-month cash flow forecast with assumptions.<br>
    · Business Tax Returns – Last 3 years of federal filings.<br>
    · Personal Financial Statement (SBA Form 413) – Required for all major owners.<br>
    · Project Cost Breakdown – Invoices, purchase agreements, or construction estimates.<br>
    · Environmental Impact Report – (Mandatory for real estate) Phase I report.<br>
    · Management Resumes – Highlighting relevant industry experience.<br>
    · Bylaws/Operating Agreement – Verification of business structure and ownership.
    </p>
    <p><u><b>References</b></u><br>
    SBA.gov. (2025). 504 Loans and Certified Development Companies. https://www.sba.gov/funding-programs/loans/504-loans<br>
    OCC.gov. (2025). SBA Small Business Development Centers: Fact Sheet. https://www.occ.gov/publications-and-resources/publications/community-affairs/community-developments-fact-sheets/pub-fact-sheet-ca-sbdc-feb-2016.pdf<br>
    America's SBDC. (2025). A Brief History of America's SBDC Network. https://americassbdc.org/about-us/a-brief-history/<br>
    Capital CDC. (2025). The SBA 7(a) and 504 Loan Insider's Guide. https://www.capitalcdc.com/uploads/images/general/2024-CCDC-7a-Guide.pdf<br>
    SBA.gov. (2025). CDC Certification and Annual Reporting Guide. https://www.sba.gov/document/sba-form-1253-certified-development-company-cdc-annual-report-guide
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def smallbusinessadministrationsbacdcsbdcfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Small Business Administration (SBA)<br>
    CDC/SBDC</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What are SBA CDCs and SBDCs?</u></b><br>
    • Answer: SBA Certified Development Companies (CDCs) and Small Business Development Centers (SBDCs) are SBA-supported organizations that provide small businesses with financing support, counseling, training, and technical assistance rather than direct lending.
    </p>
    <p><u><b>2. How do CDCs differ from SBDCs?</u></b><br>
    • Answer: CDCs primarily focus on facilitating SBA 504 loans for fixed assets, while SBDCs focus on free or low-cost business advising, training, and operational support.
    </p>
    <p><u><b>3. Do CDCs and SBDCs provide direct funding to businesses?</u></b><br>
    • Answer: CDCs do not lend directly but partner with banks to deliver SBA 504 loans, while SBDCs do not provide funding and instead offer advisory and educational services.
    </p>
    <p><u><b>4. What types of businesses are best suited for CDC support?</u></b><br>
    • Answer: Established small businesses seeking to purchase or improve fixed assets such as real estate or equipment are best suited for CDC-supported SBA 504 financing.
    </p>
    <p><u><b>5. What types of businesses benefit most from SBDC services?</u></b><br>
    • Answer: Startups, early-stage businesses, and growing small businesses benefit most from SBDCs through business planning, financial guidance, and operational support.
    </p>
    <p><u><b>6. How much financing can be accessed through CDC-supported SBA 504 loans?</u></b><br>
    • Answer: SBA 504 loans facilitated by CDCs can provide up to several million dollars in long-term, fixed-rate financing for eligible projects.
    </p>
    <p><u><b>7. How quickly can businesses access support from CDCs or SBDCs?</u></b><br>
    • Answer: SBDC advisory services can often be accessed immediately, while CDC-facilitated financing typically takes several weeks to months due to loan structuring and approvals.
    </p>
    <p><u><b>8. What are the costs of using CDC or SBDC services?</u></b><br>
    • Answer: SBDC services are usually free or low-cost, while CDC-supported loans involve standard SBA and lender fees associated with SBA 504 financing.
    </p>
    <p><u><b>9. Do CDCs or SBDCs require equity or ownership in the business?</u></b><br>
    • Answer: No, neither CDCs nor SBDCs require equity, as they are public support organizations rather than investors.
    </p>
    <p><u><b>10. Can startups work with CDCs or SBDCs?</u></b><br>
    • Answer: Startups commonly work with SBDCs for guidance, but CDC financing generally requires an operating history and is less accessible to very early-stage startups.
    </p>
    <p><u><b>11. What kind of assistance do SBDCs provide?</u></b><br>
    • Answer: SBDCs provide help with business plans, financial projections, marketing strategies, loan packaging, compliance, and general business management.
    </p>
    <p><u><b>12. How do CDCs support economic development?</u></b><br>
    • Answer: CDCs promote economic development by facilitating long-term financing for projects that create jobs, support local communities, and strengthen regional economies.
    </p>
    <p><u><b>13. Can CDC or SBDC support be combined with other funding sources?</u></b><br>
    • Answer: Yes, CDC-facilitated loans are commonly combined with bank financing and owner equity, and SBDC guidance can complement grants, loans, or private investment.
    </p>
    <p><u><b>14. Are there risks associated with relying on CDC or SBDC support?</u></b><br>
    • Answer: Risks are minimal, but businesses must meet SBA eligibility requirements, comply with loan terms, and avoid relying solely on advisory support without execution.
    </p>
    <p><u><b>15. How can a business maximize the value of CDC and SBDC programs?</u></b><br>
    • Answer: Businesses can maximize value by engaging early, using SBDC counseling to prepare strong financials, and leveraging CDC expertise to structure compliant and cost-effective SBA financing.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def smallbusinessadministrationsbacdcsbdctwelve(request):
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
    Capital Type: CDC/SBDC</p></center>
    <p><b><u>1 - Stage of Development Assessment</u></b><br>
    CDC (Certified Development Companies) and SBDC (Small Business Development Centers) support all stages of business development, from idea-stage startups to mature, expanding businesses. They are especially valuable during formation, growth planning, and capital readiness phases.
    </p>
    <p><b><u>2 - Entity Type Assessment</u></b><br>
    Eligible entities include sole proprietorships, partnerships, LLCs, S-Corps, and C-Corps. Eligibility is broad, as these programs focus on business viability and compliance, not ownership structure.
    </p>
    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    There are no minimum capital requirements. Businesses may have no prior funding or may already have debt or equity. The focus is on improving financial readiness and eligibility for SBA or bank financing.
    </p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    CDC/SBDC services operate outside capital markets. They do not provide equity or loans directly (except CDCs in SBA 504 structures), but help businesses access commercial, SBA-backed, or government financing.
    </p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    CDC and SBDC programs do not cap the amount of capital a business may pursue. Instead, they help align businesses with appropriate funding sources, including SBA 7(a), SBA 504, grants, or bank loans.
    </p>
    <p><b><u>6 - Capital Round Assessment</u></b><br>
    These programs are not tied to investment rounds. They support businesses before, during, and after capital raises by strengthening documentation, financials, and lender readiness.
    </p>
    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    There is no tranche structure, as CDC/SBDC support is advisory and facilitative. Engagements may occur over multiple sessions or milestones depending on business needs.
    </p>
    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    When tied to CDC-led SBA 504 financing, funds must follow strict SBA asset-use rules. For SBDC support, assistance focuses on:<br>
    · Business planning and financial modeling<br>
    · Loan packaging and lender preparation<br>
    · Market research and strategy<br>
    · Compliance and operational improvement
    </p>
    <p><b><u>9 - Risk Assessment</u></b><br>
    Risk is low, as no capital is directly borrowed or invested through SBDC services. For CDC-facilitated loans, standard debt repayment and compliance risks apply.
    </p>
    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    SBDC services are typically free or low-cost, funded by the SBA. CDC-related costs apply only when used in SBA 504 loan structures, where long-term fixed-rate debt applies without equity dilution.
    </p>
    <p><b><u>11 - Up Front Cost Assessment</u></b><br>
    Upfront costs are generally none or minimal for SBDC services. CDC involvement may involve application, legal, or processing fees if tied to SBA financing.
    </p>
    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
    SBDC advisory support can begin immediately. When used to support SBA or bank financing, timing to capital depends on the loan program, typically ranging from 30 to 120 days.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
