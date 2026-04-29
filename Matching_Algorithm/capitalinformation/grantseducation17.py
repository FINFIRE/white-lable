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

def grantseducation(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Grants</b></u><br>
    Capital Type: Education Grants </center></p>
    <p><b><u>Introduction</u></b><br>
Education Grants are ideal for organizations and startups seeking early-stage support for educational initiatives, including curriculum development, ed-tech innovation, and community outreach. They are designed so that government-supported programs, private foundations, or corporate social responsibility (CSR) wings can help projects grow and achieve impact without the need for repayment. {n} fits that definition. Education grants have been a cornerstone of sector growth for decades. For example, in 2023, the Bill & Melinda Gates Foundation awarded billions in grants, a significant portion of which targeted global education and K-12 systems to improve student outcomes. The Erasmus+ program in the European Union has a budget exceeding €26 billion for 2021-2027, supporting millions of students and thousands of educational institutions. In the U.S., the Department of Education's SBIR program provides up to $1.1 million in non-dilutive funding to small businesses to develop innovative educational technologies. On average, recipients of education grants gain access to between $50,000 and $250,000 in initial funding, alongside access to pedagogical experts and institutional networks.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.Education grants are non-repayable funds disbursed by government agencies, foundations, or corporations to support educational research, infrastructure, or innovation. Unlike loans, these funds do not accrue interest, and unlike venture capital, they do not require the founder to give up equity. These grants are often mission-driven, prioritizing societal outcomes—such as closing the achievement gap or increasing STEM literacy—over immediate financial returns. (Grants.gov, 2024)
<br>


    <br>2.  The best type of entities to raise money via education grants are non-profits, ed-tech startups, and research institutions focused on solving specific learning challenges or expanding access to underserved populations. These entities typically have a clear theory of change, a pilot program or prototype, and a commitment to measuring educational outcomes. Grants are particularly well-suited for high-risk, high-impact innovations in pedagogy where private market ROI may be slow or uncertain. (National Endowment for the Humanities, 2023)
<br>

    <br>3. Education grants emerged in their modern form during the mid-20th century as governments recognized education as a primary driver of national security and economic prosperity. The model evolved from simple scholarship programs to complex funding vehicles for systemic reform and technological integration. Historically, programs like the Fulbright Program (est. 1946) and the Title I grants in the U.S. set the stage for large-scale public investment in learning. Over the last decade, the rise of "Philanthro-capitalism" has seen private foundations adopt grant models to catalyze rapid innovation in digital learning and personalized education. (Philanthropy News Digest, 2022)
<br>
    <br>4.While education grants offer "free" capital, there are significant risks and administrative burdens. The application process is notoriously labor-intensive, often requiring months of preparation with a low statistical probability of success. Furthermore, grant funding is frequently "restricted," meaning it can only be used for specific project costs rather than general operations. Organizations may also face "grant dependency," where their mission drifts to align with available funding cycles rather than their original purpose. (The Chronicle of Philanthropy, 2023)
<br>
    <br>5.
To raise capital via an education grant, a company or organization must demonstrate a rigorous evidence-based approach, scalability, and direct alignment with the grantor's specific objectives. Most applications require a detailed project narrative, a logical framework (LogFrame), and a transparent budget. Applicants must often prove they have the administrative capacity to manage the funds and meet strict reporting milestones. Success in the competitive selection process hinges on a compelling "Statement of Need" and a clear plan for sustainability after the grant period ends. (Foundation Directory, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Grants.gov. (2024). Federal Grants for College or Career/Trade School. <a href="https://studentaid.gov/understand-aid/types/grants">https://studentaid.gov/understand-aid/types/grants</a>
<br>
    <br>National Endowment for the Humanities (NEH). (2023). Public Humanities Projects 2025 Funding Opportunity. <a href="https://www.neh.gov/grants">https://www.neh.gov/grants</a>
<br>
    <br>Philanthropy News Digest. (2022). Trends in Education Philanthropy Benchmarking. <a href="https://philanthropynewsdigest.org/">https://philanthropynewsdigest.org/</a>
<br>
    <br>The Chronicle of Philanthropy. (2023). Navigating Fundraising Uncertainty and Grant Dependency. <a href="https://www.philanthropy.com/">https://www.philanthropy.com/</a>
<br>
    <br>Foundation Directory. (2025). How to Raise Capital: Education Grants Criteria. <a href="https://fconline.foundationcenter.org/">https://fconline.foundationcenter.org/</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Registered Legal Entity - Must be a registered non-profit (e.g., 501(c)(3)), educational institution, or eligible for-profit business
<br>•   Tax-Exempt Status/Good Standing - Must provide proof of tax compliance and current legal status
<br>•   Mission Alignment - The organization's governing documents must align with educational purposes
<br>•   Financial Integrity - No history of financial mismanagement or debarment from receiving public funds
<br>•   Geographic Eligibility - Must operate within the specific regions or jurisdictions defined by the grantor
<br>•   Policy Compliance - Compliance with student privacy laws (e.g., FERPA/GDPR) and child protection policies
<br>•   Audit Readiness - Capacity to undergo financial audits as required by government or private oversight
<br>•   Conflict of Interest Disclosure - Must disclose any relationships between the applicant and the grant-making body


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Grant Proposal/Narrative - A detailed description of the project, goals, and expected outcomes
<br>•   Detailed Project Budget - A line-item breakdown of how every dollar of the grant will be spent
<br>•   IRS Determination Letter - Proof of tax-exempt status (for non-profits)
<br>•   Board of Directors List - Bios and affiliations of the governing board members
<br>•   Letters of Support - Commendations from community partners, schools, or stakeholders
<br>•   Logic Model or Theory of Change - Visual representation of how activities lead to educational impact
<br>•   Audited Financial Statements - The most recent year's financial health report
<br>•   Monitoring & Evaluation (M&E) Plan - The framework for measuring and reporting project success

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def grantseducationfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Grants<br>
    Education Grants</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What are education grants, and how do they work?</u></b><br>
    •Answer: Education grants are non-repayable funds provided by governments, public institutions, universities, foundations, or international organizations to support education-related activities. Unlike loans or equity funding, education grants do not require repayment or ownership dilution, provided that grant conditions are met.
</p>

    <p><u><b>2. Who is eligible to apply for education grants?</u></b><br>
    •Answer: Eligibility varies by program but commonly includes educational institutions, universities, research centers, non-profit organizations, NGOs, startups in the ed-tech sector, and sometimes individual researchers or students.
</p>

    <p><u><b>3. What types of projects are typically funded by education grants?</u></b><br>
    •Answer: Education grants commonly fund projects such as academic research, digital learning platforms, teacher training programs, curriculum innovation, vocational training, STEM education initiatives, scholarships, and inclusion-focused programs.
</p>

    <p><u><b>4. How much funding can be received through education grants?</u></b><br>
    •Answer: Funding amounts vary widely. Small education grants may range from $5,000 to $50,000, while larger institutional or international grants can exceed $500,000 or more.
</p>

    <p><u><b>5. How long does it take to receive funding after approval?</u></b><br>
    •Answer: Once approved, funding timelines vary but generally range from 1 to 6 months. Some grants disburse funds upfront, while others release funding in phases based on progress reports or deliverables.
</p>

    <p><u><b>6. Do education grants require repayment or equity?</u></b><br>
    •Answer: No, education grants do not require repayment and do not involve equity dilution. However, recipients must comply with grant terms, including reporting, financial transparency, and proper use of funds.
</p>

    <p><u><b>7. Are there restrictions on how grant funds can be used?</u></b><br>
    •Answer: Yes, education grants come with strict usage guidelines. Funds are usually restricted to approved budget categories such as personnel, materials, research expenses, training costs, or technology development.
</p>

    <p><u><b>8. Can education grant recipients access other funding sources simultaneously?</u></b><br>
    •Answer: Yes, most education grant programs allow recipients to combine grant funding with other sources. However, applicants must disclose all funding sources, and some grants prohibit double-funding for the same expense.
</p>

    <p><u><b>9. What are the key benefits of education grants compared to loans or equity funding?</u></b><br>
    •Answer: Education grants offer non-dilutive, non-repayable capital, reducing financial risk and supporting long-term social impact. They are especially beneficial for early-stage or non-profit education projects.
</p>

    <p><u><b>10. What reporting and compliance requirements are involved?</u></b><br>
    •Answer: Grant recipients are typically required to submit periodic progress reports, financial statements, impact assessments, and final project evaluations.
</p>

    <p><u><b>11. What happens after the education grant period ends?</u></b><br>
    •Answer: After the grant period concludes, recipients submit a final report summarizing outcomes, financial usage, and impact. Some grant providers offer follow-up funding, scaling opportunities, or long-term partnerships.
</p>

    <p><u><b>12. Are there risks associated with education grants?</u></b><br>
    •Answer: Yes, risks include administrative burden, strict compliance requirements, limited flexibility in fund usage, and dependency on grant timelines.
</p>

    <p><u><b>13. How do education grants compare to other public funding options?</u></b><br>
    •Answer: Compared to loans, education grants carry no repayment obligation. Education grants are more suitable for academic, social, or long-term educational initiatives rather than high-growth commercial ventures.
</p>

    <p><u><b>14. What organizations commonly provide education grants?</u></b><br>
    •Answer: Education grants are commonly provided by national governments, ministries of education, public universities, international organizations (e.g., UNESCO, World Bank), foundations, and development agencies.
</p>

    <p><u><b>15. How can applicants increase their chances of securing an education grant?</u></b><br>
    •Answer: Applicants can improve success by clearly aligning their project with the grant's objectives, demonstrating measurable educational impact, presenting a realistic budget, and showcasing institutional capacity or expertise.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def grantseducationtwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Grants</b></u><br>
    Capital Type: Education Grants</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Education grants are best suited for organizations or individuals at the idea, pilot, or early implementation stage. These grants commonly support curriculum development, research, teacher training, infrastructure improvement, scholarships, or educational innovation projects. They are ideal before large-scale commercialization or revenue generation, as grants prioritize educational impact over profitability.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Eligible entity types typically include nonprofit organizations, educational institutions, public schools, universities, research institutes, and sometimes individuals (students or researchers). For-profit entities may qualify only if the grant program explicitly allows them and if the project demonstrates strong educational or social value.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Education grants generally do not require prior capital and often favor applicants with limited financial resources. Programs typically assess financial sustainability and the applicant's ability to manage funds responsibly rather than total capital raised.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Grants are non-dilutive and are not affected by prior equity or debt financing. However, some education grants may restrict applicants who have received overlapping grants for the same purpose. Transparency about previous funding sources is essential to avoid duplication.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Education grants usually support specific, budgeted projects rather than large capital raises. Grant amounts can range from small awards ($5,000-$25,000) to large institutional grants ($100,000+). Applicants must clearly define the total project cost and explain how grant funds fit within the overall financial plan.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Education grants do not follow traditional funding rounds. Instead, funding is project-based and milestone-driven. Applicants may apply for multiple grants over time, but each grant is evaluated independently based on objectives, outcomes, and alignment with the grantor's mission.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds are often released in tranches tied to milestones, reporting requirements, or academic periods. Some grants provide upfront disbursement, while others release funds in phases after progress reviews, performance reports, or audits.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Grant funds are strictly restricted to approved educational purposes such as:
<br>•   Instructional materials and research expenses
<br>•   Faculty or trainer compensation
<br>•   Infrastructure upgrades and scholarships
<br>•   Program delivery costs
Funds cannot be used for personal expenses, unrelated business activities, profit distribution, or debt repayment.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
The primary risks include non-compliance with grant conditions, reporting failures, project delays, or failure to meet stated outcomes. Misuse of funds can lead to repayment obligations or disqualification from future grants.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
Education grants have very low capital cost, as they are non-dilutive and non-repayable. The main "cost" is administrative—time spent on proposal writing, reporting, audits, and compliance.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Most education grants have minimal upfront costs, though applicants may incur expenses related to proposal preparation, documentation, certifications, or compliance requirements.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
The timeline to receive funds can be moderate to long, typically ranging from 2 to 6 months after application submission, depending on the review cycle. Competitive grants may take longer due to peer reviews, academic evaluations, and administrative approvals.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
