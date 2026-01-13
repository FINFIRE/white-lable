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


def incubatorpublic(request):
    introduction = mark_safe("""<p><b><center><u>Definition of Capital Market: Incubator</u></b>
    <br>Capital Type: Public</center></p>

    <p><b><u>Introduction</u></b><br>
    The global Business Incubator market generated USD 236.49 Million revenue in 2023 <a href="https://www.thebrainyinsights.com/report/business-incubator-market-14440">(source)</a>. As per the National Business Incubation Association, startups that develop with incubator backing have an 87% chance of survival in their first five years, compared to just 44% of new businesses without such support <a href="https://www.futurize.studio/blog/are-business-incubators-worth-joining">(source)</a>.</p>

    <p><b><u>Definition of Capital Type</u></b><br>
    1) Incubators focus on startups that don’t necessarily have a business plan or model in place. Services provided by incubators include office space, administrative functions, education and mentorship, access to investors and capital, and idea generation. Incubators either charge a fee for their service or take an equity stake in the startup. The period of incubation can last from a few months to several years. Incubators focus on companies that are just starting to develop their idea into a business while accelerators take startups with an established business model and accelerate their time to market. (Smith, 2021)<br><br>

    2) Public sector incubators represent a pivotal shift in the way governments approach economic development and innovation. Unlike their private counterparts, these incubators are not solely focused on profitability but rather on fostering public good through support of startups and entrepreneurs. They serve as a bridge between the innovative potential of private enterprises and the strategic objectives of the public sector, aiming to create a symbiotic relationship that benefits society at large. By providing resources, mentorship, and access to networks, public sector incubators catalyze the growth of businesses that can address societal challenges, contribute to public policy objectives, and drive economic growth in areas that align with government priorities.<br><br>

    Public sector incubators are not just facilitators of business growth; they are enablers of societal transformation. By aligning the innovative drive of the private sector with the strategic goals of the public sector, they create a powerful platform for collaborative entrepreneurship that can lead to substantial economic, social, and technological advancements. (Public Sector Incubators: Building Bridges: Public Sector Incubators and Collaborative Entrepreneurship, 2024)<br><br>

    Public incubators are typically funded by government agencies, non-profits, or universities. Their goal is often to support economic development, innovation, and entrepreneurship. As a result:<br>
    • Lower Upfront Costs: Public incubators tend to have lower upfront costs, as they are subsidized by public funding. They may charge nominal fees for services such as rent, mentorship, and administrative costs.<br>
    • Free or Low-Cost Services: Many public incubators offer free or low-cost access to office space, facilities, and resources. This can significantly reduce the initial financial burden on entrepreneurs.<br>
    • Equity-Free: Public incubators generally do not take equity in your company. Instead, their focus is on fostering business growth and economic impact, not on financial return.<br>
    • Application Fees: Some public incubators may charge a small application fee to cover administrative costs, but these fees are usually modest compared to private incubators.<br><br>

    3) One of the benefits of being part of an incubator is the ability to access a wide range of resources that may not be available to individual entrepreneurs. These resources can include legal and accounting services, marketing and branding support, and access to funding through venture capitalists or angel investors.<br><br>

    Another key component of the incubator model is the focus on education and training. Incubators often offer workshops and seminars on topics such as business planning, financial management, and marketing strategies. These educational opportunities can be invaluable for entrepreneurs who are just starting out and may not have a background in business. (Beaver, 2023)<br><br>

    4) Incubators work on an open-ended time frame. There is no set schedule or period in which they deem a startup is ready to launch. They create an environment in a co-working space for an exchange of ideas with a multitude of selected companies that all share in overhead costs, which helps foster collaboration and the growth of relationships with like-minded individuals.<br><br>

    The startups chosen for the incubator program can expect to work with advisors and mentors who will offer their experience in the business world to help address questions and dilemmas they face. Incubator firms might put these startups through classroom-style sessions, wherein the teams must perform tasks such as gathering feedback from potential customers about their product.<br><br>

    Throughout the incubator process, the startups will be pushed to improve their ideas and learn how to convey their plans to customers and potential investors alike. It is not uncommon for startups to pivot during an incubator program after conferring with seasoned experts and testing their product or service with the public.<br><br>

    At the end of a cohort’s program, the startups will often present their business plans at a demo day session. Such an event brings together potential investors and other entrepreneurs who may wish to collaborate with or back the development of the startup. (Kenton, 2021)<br><br>

    <p><b><u>References</u></b><br>
    Beaver, C. (2023, April 20). A Comprehensive Guide to the Startup Incubator Business Model. Retrieved from Advisory Cloud: <a href="https://advisorycloud.com/blog/a-comprehensive-guide-to-the-startup-incubator-business-model">https://advisorycloud.com/blog/a-comprehensive-guide-to-the-startup-incubator-business-model</a><br>
    Kenton, W. (2021, October 26). How an Incubator Firm Helps Develop Early-Stage Companies. Retrieved from Investopedia: <a href="https://www.investopedia.com/terms/i/incubatorfirm.asp">https://www.investopedia.com/terms/i/incubatorfirm.asp</a><br>
    Public Sector Incubators: Building Bridges: Public Sector Incubators and Collaborative Entrepreneurship. (2024, June 19). Retrieved from Faster Capital: <a href="https://fastercapital.com/content/Public-Sector-Incubators--Building-Bridges--Public-Sector-Incubators-and-Collaborative-Entrepreneurship.html">https://fastercapital.com/content/Public-Sector-Incubators--Building-Bridges--Public-Sector-Incubators-and-Collaborative-Entrepreneurship.html</a><br>
    Smith, T. D. (2021). Business Capital 101. San Francisco: Imaginary Press.</p>

    <p><b><u>Legal Qualification Requirements</u></b></p>
    <p>• Legal Entity Type - Must be a legally incorporated entity (C-Corp, LLC, etc.), preferably a C-Corp for scalability and investment ease.<br>
    • Company Formation and Registration - Business must be registered and in good standing within its jurisdiction, complying with local incorporation laws.<br>
    • Compliance with Applicable Laws - Must comply with local, state, and federal laws, including tax, labor, and regulatory requirements.<br>
    • Intellectual Property Ownership - Must own or have exclusive rights to intellectual property (patents, trademarks, etc.) if applicable.<br>
    • Founder Eligibility - Founders must be legally competent and free from disqualifications (e.g., criminal convictions, bankruptcies).<br>
    • Legitimate Business Activity - Must operate in a legal and ethical sector, aligning with the incubator’s focus or industry.<br>
    • Securities Law Compliance - Must adhere to securities laws for capital raising, including private placement rules and accreditation requirements for investors.<br>
    • Financial Transparency - Should have clear financial records in compliance with accounting standards, disclosing liabilities, debts, and investors.<br>
    • Stage of Business - Typically early-stage businesses with proven products/services and scalable potential.<br>
    • Governance Structure - Must have a formal governance structure, such as a board of directors or equivalent management team.<br>
    • Location Requirements - May need to be based in a specific region or country depending on the incubator's geographic focus.<br>
    • Legal Standing - Must not be involved in ongoing legal disputes or litigation that could affect operations.<br>
    • Social Impact Alignment - Some incubators may require alignment with public benefit goals or contributions to social good objectives.</p>

    <p><b><u>Supporting Document List</u></b></p>
    <p>• Business Plan - A detailed plan covering mission, market strategy, financial projections, and growth plans.<br>
    • Legal Entity Documents - Articles of Incorporation, operating agreement/bylaws, and EIN confirmation.<br>
    • Intellectual Property - Documentation of ownership or licenses for patents, trademarks, etc.<br>
    • Financial Statements - Income statement, balance sheet, cash flow statement, and tax returns for the past 1-3 years.<br>
    • Investor Documents - Capitalization table, prior investment agreements, and shareholder agreements.<br>
    • Securities Offering Documents - Private placement memorandum and investor accreditation forms (if applicable).<br>
    • Legal Compliance - Certificate of good standing, necessary business licenses, and regulatory approvals.<br>
    • Founder & Executive Background - Resumes, bios, and background checks for key personnel.<br>
    • Market Research & Validation - Customer demand data, LOIs, MOUs, and pilot program results.<br>
    • Use of Funds Statement - Detailed breakdown of how the raised capital will be used.<br>
    • Board/Advisory Board - Board resolutions and advisory agreements, if applicable.<br>
    • Exit Strategy - Plan for providing returns to investors (e.g., acquisition, IPO).<br>
    • Non-Disclosure Agreements (NDAs) - NDAs for protecting sensitive information during the process.<br>
    • Application Form - Incubator-specific application form and any additional requested information.<br>
    • Compliance Certifications - Anti-Money Laundering (AML) and Know Your Customer (KYC) certifications, if required.</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def incubatorpublicfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Incubator<br>
    Capital Type: Public</center></p>                        
    <p><center><u><b>Frequently Asked Question for Public Incubator</u></b></center></p>
                             
    <p><u><b>1. What is a public incubator, and how does it differ from private incubators or accelerators?</b></u><br></p>
    <p>A public incubator is a government or publicly funded program designed to support startups and early-stage companies through resources like funding, mentorship, office space, and access to networks. Unlike private incubators, which are often run by venture capitalists or other private entities with profit motives, public incubators are typically focused on fostering innovation, job creation, and economic growth. The funding is often less risky and more accessible for businesses.</p>

    <p><u><b>2. What are the key benefits of raising capital through a public incubator?</b></u><br></p>
    <p>Public incubators offer several advantages, including:</p>
    <ul>
      <li>Low-cost or free access to resources like office space, administrative support, and business services.</li>
      <li>Government funding or grants with fewer strings attached compared to venture capital or private funding.</li>
      <li>Mentorship and networking from industry experts, policymakers, and other startups.</li>
      <li>Tax incentives or subsidies designed to foster innovation and growth.</li>
      <li>Reduced financial pressure, as public incubators often don’t require equity stakes or impose high interest rates.</li>
    </ul>

    <p><u><b>3. How do I qualify for a public incubator program?</b></u><br></p>
    <p>Eligibility requirements vary by incubator, but generally, businesses must:</p>
    <ul>
      <li>Be in the early stages of development or have a viable product idea.</li>
      <li>Focus on innovation or technology development.</li>
      <li>Be located within the geographic area covered by the incubator (local, regional, or national).</li>
      <li>Demonstrate potential for economic impact, job creation, or alignment with government priorities.</li>
      <li>It’s important to check the specific criteria of each incubator program.</li>
    </ul>

    <p><u><b>4. What types of funding are available through public incubators?</b></u><br></p>
    <p>Public incubators typically offer:</p>
    <ul>
      <li>Seed funding or grants for research and development, product validation, or market entry.</li>
      <li>Matching grants where the government matches private investments or other funding sources.</li>
      <li>Convertible notes or low-interest loans, often with more favorable terms compared to private investors.</li>
      <li>Equity-free funding where businesses don’t have to give up ownership in exchange for capital.</li>
      <li>It’s crucial to understand the terms and conditions attached to each type of funding.</li>
    </ul>

    <p><u><b>5. Are there any equity requirements or ownership stakes taken by the incubator?</b></u><br></p>
    <p>Unlike venture capital firms, most public incubators do not take equity in exchange for funding. However, some programs may ask for minimal ownership (e.g., 1-5%) or require companies to meet specific milestones for continued support. It’s important to confirm this upfront to avoid unexpected surprises.</p>

    <p><u><b>6. How does a public incubator impact my business’s autonomy and decision-making?</b></u><br></p>
    <p>Most public incubators allow businesses to retain full control over their operations and decision-making, as their primary goal is to provide support, not dictate business strategies. However, incubators may offer mentorship or require milestone reporting. In exchange for capital, there might be oversight or guidelines to ensure the incubator’s investment objectives are met.</p>

    <p><u><b>7. How much funding can my company expect to raise through a public incubator?</b></u><br></p>
    <p>The amount of funding provided varies depending on the program. Some incubators may offer small grants of a few thousand dollars, while others may offer larger sums or match your own private funding. It’s important to research each incubator’s funding limits and requirements before applying.</p>

    <p><u><b>8. What kind of mentorship and support can I expect from a public incubator?</b></u><br></p>
    <p>In addition to funding, public incubators provide valuable resources, including:</p>
    <ul>
      <li>Business mentorship from seasoned entrepreneurs, industry experts, and government advisors.</li>
      <li>Access to professional services like legal, financial, and marketing support.</li>
      <li>Networking opportunities with investors, other startups, and potential customers.</li>
      <li>Training programs on various aspects of business development, such as marketing, scaling, and fundraising.</li>
      <li>These can be invaluable in helping your business grow and thrive.</li>
    </ul>

    <p><u><b>9. How long does the support last once I join an incubator?</b></u><br></p>
    <p>The length of support varies by incubator, but most public incubators offer programs lasting 6 months to 2 years. After the program, businesses may continue to receive ongoing support, though this depends on the specific incubator’s structure. Some incubators may offer graduation pathways where startups move on to more advanced programs or have access to alumni networks.</p>

    <p><u><b>10. Can I apply to multiple public incubators simultaneously?</b></u><br></p>
    <p>In many cases, yes, but it depends on the rules of each incubator. Some may allow participation in more than one program, while others might have exclusive requirements. Additionally, there could be conflict-of-interest clauses if the incubators are funded by different government agencies or have competing objectives. Always check the application guidelines carefully.</p>

    <p><u><b>11. What are the potential risks or drawbacks of using a public incubator?</b></u><br></p>
    <p>While public incubators offer many advantages, there are some potential downsides to consider:</p>
    <ul>
      <li>Limited flexibility in terms of funding and program offerings compared to private incubators or venture capital.</li>
      <li>Slow application and funding processes, which can delay access to capital.</li>
      <li>Administrative oversight or regulatory requirements that could create additional bureaucracy.</li>
      <li>High competition for spots in incubators, making it difficult to gain entry.</li>
    </ul>

    <p><u><b>12. How does a public incubator align with my long-term capital-raising strategy?</b></u><br></p>
    <p>A public incubator is an excellent way to secure early-stage funding and mentorship. If your company is seeking long-term capital after incubator support, it’s likely to be positioned to attract venture capital or angel investment. Public incubators can help you build credibility, refine your business model, and develop a network that will appeal to private investors.</p>

    <p><u><b>13. What happens after the incubator program ends?</b></u><br></p>
    <p>After completing the program, you may:</p>
    <ul>
      <li>Continue to benefit from alumni networks, ongoing mentorship, or access to further funding opportunities.</li>
      <li>Be better prepared to approach private investors, as incubator graduates often have stronger business plans and product-market fit.</li>
      <li>Potentially be eligible for follow-on funding from government programs or investors that prefer to back incubator graduates.</li>
    </ul>

    <p><u><b>14. How do I apply to a public incubator?</b></u><br></p>
    <p>Each public incubator has its own application process, but typically, you will need to submit a business plan, financial projections, and a clear vision of how the funding will be used. It’s important to make your application as comprehensive and compelling as possible, highlighting your company’s innovation, scalability, and impact potential.</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def incubatorpublictwelve(request):
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
    <center><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</u></b><br>
    Incubator - Public Incubator</center>

    <p><b><u>1 - Stage of Development Assessment</u></b><br>While public incubators can support companies at different stages, the ideal stage is typically early-stage—ranging from the pre-seed stage (idea phase) to the early growth or pre-revenue stage. At these points, startups need substantial help with funding, mentoring, product development, and scaling, all of which public incubators excel at providing.</p>

    <p><b><u>2 - Entity Type Assessment</u></b><br>LLCs and C-Corps are generally the best-suited entity types for utilizing public incubators due to their flexibility, ability to raise capital, and scalability. However, nonprofits or social enterprises with a clear mission can also benefit greatly from incubator support, especially when focused on public good.</p>

    <p><b><u>3 - Pre-Capital Assessment</u></b><br>While there are no universal limits on the amount of pre-capital raised to apply for an incubator, each incubator has a unique set of criteria. If a company has already raised substantial capital, they may be better suited for growth-stage incubators or programs focused on scaling, rather than programs focused on seed or early-stage innovation. Restrictions may include:<br>
        • Early-Stage Focus: Many public incubators focus on startups at the pre-seed or seed stage, so companies that have raised substantial capital (e.g., over $500,000–$1 million) may not qualify.<br>
        • Type of Capital Raised: Startups that have raised venture capital or large equity investments may not be eligible, while those with grants or non-equity funding may still qualify.<br>
        • Program Type: The incubator’s stage-specific focus (early-stage vs. growth-stage) will determine whether a company with pre-existing funding is eligible.<br>
        • Grant and Funding Caps: Some public incubators or government funding programs have caps on the amount of capital a company can have raised before applying.</p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>There can be restrictions or limitations based on how companies have raised pre-capital that could interfere with their ability to use a public incubator. These restrictions typically revolve around the type of capital raised, the stage of funding, and whether the funding aligns with the incubator’s mission, goals, and eligibility criteria. Some of the restrictions could be:<br>
        • Equity Financing: Startups that have already raised significant venture capital or angel investment may be excluded from incubators that focus on early-stage companies needing further seed funding.<br>
        • Debt Financing: Excessive debt financing could be a concern for public incubators, especially if it places undue financial pressure on the startup.<br>
        • Government or Public Funding: Companies that have already accessed government grants or subsidies may face restrictions to avoid duplication of public funding resources.<br>
        • Private Investment: Companies with substantial private investment may be excluded from public incubators, as they might already be ready to raise capital through private venture funds.<br>Ultimately, the key to eligibility is whether the company's funding aligns with the goals and mission of the public incubator, as well as the stage of development the incubator targets. It's important for businesses to carefully review the incubator's eligibility criteria to understand the impact of their pre-capital raising activities on their ability to join the program.</p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>The amount a company can raise through a public incubator depends on factors like the stage of development, the type of incubator, the sector of the business, and the type of funding the incubator provides (grants, equity investments, loans, etc.). Public incubators typically provide seed funding, grants, or access to private investors, and the total amount can range from small grants to significant funding in the $500,000 to $5 million range, depending on the incubator and the company’s needs.</p>

    <p><b><u>6 - Capital Round Assessment</u></b><br>the pre-seed and seed stages are the most appropriate for leveraging a public incubator. These stages align with the incubator’s focus on helping early-stage companies develop their products, refine their business models, and gain initial market traction. Once a company reaches Series A or higher, it’s typically better positioned to raise capital through private investors and venture capital, making a public incubator less relevant at that stage.</p>

    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>The ideal number of tranches when raising capital through a public incubator typically ranges from 1 to 4 tranches, with each tranche tied to specific company milestones.<br>For pre-seed to seed stage companies, 1 to 3 tranches is typical, with funding released as the company achieves early-stage milestones like product development or market validation.<br>For growth-stage companies preparing for Series A, 2 to 4 tranches may be used, often focused on scaling efforts, market expansion, or preparing for private investment.</p>

    <p><b><u>8 - Use of Funds Assessment</u></b><br>There are typically restrictions on how funds from a public incubator can be used, depending on the specific terms and conditions set by the incubator. Public incubators usually provide funding with specific guidelines to ensure that the money is used effectively to support the growth and success of the business. These restrictions are often designed to ensure the funds are applied in ways that benefit the incubator’s objectives, such as fostering innovation, scaling businesses, or creating job opportunities.</p>

    <p><b><u>9 - Risk Assessment</u></b><br>In general, businesses that engage with public incubators must have a moderate risk tolerance. Businesses that are comfortable with uncertainty, willing to embrace change, and able to take calculated risks are well-suited to benefit from the resources, mentorship, and funding that public incubators provide.</p>

    <p><b><u>10 - Capital Cost Assessment</u></b><br>When a business considers using a public incubator, the capital cost tolerance they need to have is typically moderate. The capital costs associated with using a public incubator are not just financial but also involve time, resources, and rarely equity dilution. Businesses must be prepared for certain expenses and commitments that come with the incubator’s resources, mentorship, and funding.</p>

    <p><b><u>11 - Up Front Cost Assessment</u></b><br>For most businesses using a public incubator, upfront costs typically range from $500 to $10,000 in the first year, depending on the specifics of the incubator’s program and the resources provided. For incubators that charge equity or a nominal fee, the upfront costs may be low in cash terms, but businesses need to consider the long-term implications of giving up equity and what the trade-off is for the resources, mentorship, and support provided.</p>

    <p><b><u>12 - Timing to Capital Assessment</u></b><br>A company can typically expect to receive initial capital from a public incubator within 1 to 3 months of joining, with follow-up milestone-based funding being provided after 3 to 6 months. If the business is progressing well and meeting milestones, the timeline for receiving funding can be relatively fast compared to traditional fundraising methods, but it still depends on the specific incubator, the company’s development, and the nature of the funding program.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)