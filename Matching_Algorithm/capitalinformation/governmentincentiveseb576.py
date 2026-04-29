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

def governmentincentiveseb5(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Government Incentives</b></u><br>
    Capital Type: EB5 Immigration </center></p>
    <p><b><u>Introduction</u></b><br>
EB-5 Immigration Incentives are ideal for foreign investors seeking permanent U.S. residency through capital investment that generates economic growth and job creation. They are designed so that qualifying investors contribute capital to approved U.S. commercial enterprises or regional center projects in exchange for eligibility to obtain lawful permanent resident status (a "Green Card"). {n} fits that definition. In 2026, the EB-5 Immigrant Investor Program remains a significant source of foreign direct investment into U.S. real estate, infrastructure, and operating businesses. The program is commonly used to finance large-scale development projects, particularly those located in Targeted Employment Areas (TEAs), where reduced investment thresholds apply. While EB-5 incentives provide access to U.S. residency and patient capital for projects, they introduce immigration, compliance, and execution risk. Investors must satisfy strict source-of-funds, job-creation, and timing requirements, and failure to meet program criteria can result in denial or revocation of immigration benefits.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.EB-5 Immigration is a U.S. government incentive program established under the Immigration and Nationality Act that allows foreign nationals to obtain permanent residency by investing a qualifying amount of capital in a U.S. business that creates or preserves jobs for U.S. workers. (U.S. Citizenship and Immigration Services, 2025)
<br>


    <br>2.  EB-5 capital exists outside the traditional Capital Stack, as it is motivated primarily by immigration benefits rather than financial return optimization. Investments are typically structured as equity or subordinated debt within EB-5-eligible projects. (U.S. Government Accountability Office, 2025)
<br>

    <br>3. Legally, EB-5 investments are governed by federal immigration regulations and securities laws, requiring compliance with USCIS rules, offering disclosures, and anti-fraud provisions. Projects are often sponsored by USCIS-designated Regional Centers that pool investor capital. (U.S. Department of Homeland Security, 2025)
<br>
    <br>4.From a risk perspective, EB-5 investors face immigration approval risk, project execution risk, and capital recovery risk. Delays in adjudication, insufficient job creation, or project underperformance can jeopardize immigration outcomes and investment return. (Congressional Research Service, 2025)
<br>
    <br>5.
From an accounting and process standpoint, EB-5 investments are recorded as Equity Interests or Subordinated Loans in project entities. Capital is typically locked up for multiple years and released only after job-creation and immigration milestones are satisfied. (Deloitte, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>U.S. Citizenship and Immigration Services (USCIS). (2025). EB-5 Immigrant Investor Program. <a href="https://www.uscis.gov/eb-5">https://www.uscis.gov/eb-5</a>
<br>
    <br>U.S. Government Accountability Office (GAO). (2025). Immigrant Investor Program Oversight. <a href="https://www.gao.gov">https://www.gao.gov</a>
<br>
    <br>U.S. Department of Homeland Security (DHS). (2025). EB-5 Regional Center Program. <a href="https://www.dhs.gov">https://www.dhs.gov</a>
<br>
    <br>Congressional Research Service (CRS). (2025). The EB-5 Immigrant Investor Visa. <a href="https://crsreports.congress.gov">https://crsreports.congress.gov</a>
<br>
    <br>Deloitte. (2025). Accounting and Structuring of EB-5 Investments. <a href="https://www2.deloitte.com/immigration-investment">https://www2.deloitte.com/immigration-investment</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Investor Eligibility - Foreign national meeting EB-5 criteria
<br>•   Minimum Investment Amount - Statutory threshold (TEA or non-TEA)
<br>•   Job Creation Requirement - Minimum qualifying U.S. jobs
<br>•   Source of Funds Verification - Lawful capital documentation
<br>•   USCIS Petition Approval - I-526E and I-829 filings
<br>•   Securities Law Compliance - Offering disclosures and anti-fraud rules
<br>•   Regional Center Sponsorship (if applicable) - USCIS designation
<br>•   Ongoing Compliance & Reporting - Immigration and project oversight


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   EB-5 Offering Memorandum - Project and immigration disclosures
<br>•   Subscription Agreement - Investor capital commitment
<br>•   Business Plan - Job creation and economic impact analysis
<br>•   Economic Report - Employment methodology
<br>•   Source of Funds Documentation - Investor financial records
<br>•   USCIS Petitions (I-526E, I-829) - Immigration filings
<br>•   Regional Center Approval - USCIS designation letter
<br>•   Legal Opinions - Immigration and securities compliance

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def governmentincentiveseb5faq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Government Incentives<br>
    EB5 Immigration</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is the EB-5 Immigrant Investor Program?</u></b><br>
    •Answer: The EB-5 program is a U.S. government initiative that allows foreign investors to obtain permanent residency (a Green Card) by making a qualifying investment in the U.S. economy.
</p>

    <p><u><b>2. Who administers the EB-5 program?</u></b><br>
    •Answer: The program is administered by U.S. Citizenship and Immigration Services (USCIS).
</p>

    <p><u><b>3. Who is eligible to apply under the EB-5 program?</u></b><br>
    •Answer: Foreign nationals who make a qualifying investment and meet program requirements are eligible to apply.
</p>

    <p><u><b>4. What is the minimum investment required for EB-5?</u></b><br>
    •Answer: The minimum investment is typically $800,000 in a Targeted Employment Area (TEA) or $1,050,000 in a non-TEA project.
</p>

    <p><u><b>5. What types of investments qualify under EB-5?</u></b><br>
    •Answer: Investments must be made in a new commercial enterprise that creates or preserves jobs in the United States.
</p>

    <p><u><b>6. What is a Targeted Employment Area (TEA)?</u></b><br>
    •Answer: A TEA is a rural area or an area with high unemployment, designated to encourage investment in underdeveloped regions.
</p>

    <p><u><b>7. How many jobs must an EB-5 investment create?</u></b><br>
    •Answer: Each EB-5 investment must create or preserve at least 10 full-time jobs for qualified U.S. workers.
</p>

    <p><u><b>8. What is a Regional Center in the EB-5 program?</u></b><br>
    •Answer: A Regional Center is a USCIS-approved entity that sponsors EB-5 projects and allows indirect job creation to count.
</p>

    <p><u><b>9. How does the EB-5 investment process work?</u></b><br>
    •Answer: The investor makes the investment, files an EB-5 petition, obtains conditional residency, and later applies to remove conditions after meeting requirements.
</p>

    <p><u><b>10. Is the EB-5 investment guaranteed?</u></b><br>
    •Answer: No, EB-5 investments must be "at risk," meaning there is no guarantee of return or capital preservation.
</p>

    <p><u><b>11. How long does the EB-5 process take?</u></b><br>
    •Answer: Processing times vary by country and case complexity and can range from several years to longer for high-demand countries.
</p>

    <p><u><b>12. Can family members benefit from an EB-5 investment?</u></b><br>
    •Answer: Yes, the investor's spouse and unmarried children under 21 can also obtain permanent residency.
</p>

    <p><u><b>13. What are the benefits of the EB-5 program?</u></b><br>
    •Answer: Benefits include U.S. permanent residency, access to U.S. education and employment, and freedom to live anywhere in the U.S.
</p>

    <p><u><b>14. What are the risks associated with EB-5 investments?</u></b><br>
    •Answer: Risks include investment loss, project failure, job creation shortfalls, and immigration processing delays.
</p>

    <p><u><b>15. When should an investor consider the EB-5 program?</u></b><br>
    •Answer: An investor should consider EB-5 when seeking U.S. residency and willing to make a long-term, at-risk investment aligned with program requirements.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def governmentincentiveseb5twelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Government Incentives</b></u><br>
    Capital Type: EB5 Immigration</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
EB-5 immigration investment capital is best suited for operating or development-stage projects that can demonstrate job creation, capital deployment readiness, and long-term project viability. These projects are typically at growth or mature stages rather than early startup stages, as EB-5 programs require defined business plans and employment outcomes.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Eligible entities commonly include C-Corporations, LLCs, real estate development entities, and special purpose vehicles structured to receive EB-5 capital. Projects are often sponsored through USCIS-approved regional centers. Sole proprietorships are generally not suitable due to program structure and compliance requirements.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Projects utilizing EB-5 capital usually have significant pre-capital planning, including land acquisition, permits, or partial funding already in place. While prior equity or debt investment is common, underwriting focuses more heavily on job creation potential, project feasibility, and compliance with EB-5 regulations rather than traditional capitalization metrics.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
EB-5 operates within a government-regulated immigrant investment market overseen by U.S. Citizenship and Immigration Services. Capital is sourced from foreign investors seeking permanent residency through qualified investment, rather than from traditional financial investors.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
EB-5 capital raises commonly range from several million to hundreds of millions of dollars, depending on project scale, number of investors, and job creation requirements. Individual investment minimums are defined by statute and vary based on targeted employment area designation.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
EB-5 funding is not a traditional capital round. It is structured as pooled immigrant investor capital, often layered alongside senior debt, mezzanine financing, and sponsor equity within a project's capital stack.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds are typically contributed in tranches tied to investor subscriptions, escrow release conditions, and USCIS filing milestones. Capital may be released incrementally as immigration and project requirements are satisfied.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
EB-5 capital is restricted to job-creating project costs such as:
<br>•   Construction, equipment, and payroll
<br>•   Infrastructure and operating expenses
<br>•   Costs directly tied to employment generation
Use of funds must comply strictly with approved business plans and regulatory filings.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk to investors includes immigration approval risk, project execution risk, and delayed capital return. For issuers, risk includes regulatory compliance, reporting obligations, and potential delays or restructuring if immigration or project milestones are not met.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of EB-5 capital is generally lower than market-rate mezzanine or private equity capital due to investors' immigration motivations. However, issuers incur compliance, administrative, and structuring costs that increase overall project complexity.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are high and include legal and immigration advisory fees, regional center sponsorship costs, offering documentation, compliance filings, marketing expenses, and ongoing reporting obligations. These costs are necessary to maintain program eligibility.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital is extended due to regulatory review, investor sourcing, and USCIS processing timelines. Capital deployment may begin within several months, but full funding and investor immigration outcomes can take multiple years.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
