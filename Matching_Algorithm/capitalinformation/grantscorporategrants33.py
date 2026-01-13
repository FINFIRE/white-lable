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


def grantscorporategrants(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Grants</b></u><br>
    Capital Type: Corporate Grants</center></p>
    
    <p><b><u>Introduction</u></b><br>
    Corporate grants are ideal for companies seeking non-dilutive funding to support research, innovation, community development, or socially impactful business models. These grants are typically awarded by large corporations aiming to support initiatives aligned with their corporate social responsibility (CSR) or strategic goals. {n} fits that definition. Corporate grant programs have steadily grown over the past decade; for example, in 2023, U.S. corporations contributed over $21 billion in cash and in-kind donations to nonprofits and businesses alike. Programs like Google.org, Wells Fargo Open for Business Fund, and the Verizon Small Business Digital Ready grant initiative exemplify the rising trend of businesses supporting innovation in the private sector. However, corporate grants can come with risks such as high competition, eligibility limitations, and extensive reporting requirements that may strain smaller companies.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br>1.	A corporate grant is a form of financial or in-kind contribution provided by a corporation to nonprofit organizations, educational institutions, or community projects. These grants are typically part of a company’s Corporate Social Responsibility (CSR) or philanthropic strategy, intended to support causes that align with the company’s values, community engagement goals, or brand mission.
    <br>
        <br>Corporate grants can come in many forms, including cash donations, matching gift programs, in-kind contributions (such as goods, services, or volunteer hours), and sponsorships. Unlike loans or investments, these grants are generally not expected to be repaid, and they may be restricted (for specific projects) or unrestricted (usable at the nonprofit’s discretion).
    <br>
        <br>Corporations may issue grants through:
        <br>	Corporate foundations (separate charitable arms of a business)
        <br>	CSR departments (internal units dedicated to social impact)
        <br>	Employee-led programs (e.g., matching gifts or volunteer grants)
    <br>
        <br>These grants serve multiple purposes: advancing social good, improving community relations, increasing employee engagement, and enhancing the company’s reputation. For nonprofits, corporate grants are valuable sources of funding and can lead to long-term partnerships with businesses. (Weinger, 2025)
    <br>
        <br>2.	Corporate grants come in various forms, each serving different needs and objectives for both the corporation and the nonprofit organizations they support. Direct financial grants are the most common, where a company provides a monetary donation to fund specific projects or programs. These grants can be one-time contributions or part of a multi-year commitment, typically for well-defined initiatives that align with the corporation’s mission. Another common type is matching gifts, where companies match donations made by their employees to nonprofit organizations. This type of grant incentivizes employees to give to causes they care about while also supporting the nonprofit’s fundraising efforts. In-kind contributions are another type of corporate grant, where companies donate goods or services instead of cash. For example, a software company might donate licenses to a nonprofit organization, or a construction firm may provide materials for a community development project. These types of grants help reduce operational costs for nonprofits while offering the company an opportunity to showcase their products or services.
    <br>
        <br>Additionally, many companies offer employee volunteer grants to encourage community involvement. In this case, a corporation provides a grant to a nonprofit organization based on the number of hours their employee's volunteer. The grant is typically given after the employee logs a certain amount of volunteer time, helping nonprofits gain additional funding while encouraging employee engagement. Program-related investments (PRIs) are also a unique form of corporate grant, where companies (usually through their foundations) make investments aimed at supporting social programs or organizations. These investments may be repayable, unlike traditional grants, and often focus on projects that have a measurable social impact. Finally, event sponsorships are a form of corporate grant where a company financially supports nonprofit events, such as fundraisers, charity auctions, or community festivals, in exchange for brand exposure and recognition. This type of grant not only provides necessary funding but also offers marketing opportunities for the sponsoring corporation. (Huntsberger, 2025)
    <br>
        <br>3.	The history of corporate grants dates back to the early 20th century, when large corporations began to recognize the importance of giving back to society. Early examples of corporate philanthropy were often linked to the personal beliefs of business owners or the desire to improve public relations. One of the earliest and most well-known examples was the establishment of the Ford Foundation in 1936 by Henry Ford and his son Edsel Ford. This marked a shift towards more formalized corporate giving. During the post-World War II era, corporations began to increasingly view philanthropy as an essential aspect of their operations, not just as a way to promote goodwill but also as part of their broader social responsibility. The 1970s saw the formalization of corporate foundations as separate entities dedicated to charitable giving. By the late 20th century, corporate grants had evolved into a key component of Corporate Social Responsibility (CSR) programs, with companies focusing on causes like education, healthcare, environmental sustainability, and community development. Today, corporate grants are a major source of funding for nonprofits, with businesses using them as a strategic tool to both address social issues and enhance their brand reputation. (Dunn, 2023)
    <br>
        <br>4.	While corporate grants can provide valuable funding for nonprofits, startups, and community organizations, they also come with several risks that recipients should carefully consider. One major concern is mission drift, where organizations alter their programs or goals to align with the corporation’s interests, potentially compromising their core values. There's also a significant reputational risk in partnering with corporations that may be involved in controversial practices, as public association with such companies can damage trust with stakeholders or the broader community. Additionally, corporate grants are often short-term or one-time funding sources, which can create financial instability if an organization becomes too reliant on them without developing diverse revenue streams. Many grants also come with strict conditions or reporting requirements, which can increase administrative workload and divert resources from program delivery. Lastly, the unpredictability of corporate budgets—subject to market fluctuations and internal changes—means that grant renewals are never guaranteed, leaving recipients vulnerable to sudden funding gaps. (Society for Non-Profits, n.d.)
    <br>
    <br>5.	To qualify for a corporate grant, a company typically needs to meet several key requirements. First and foremost, the business should have a clear mission or project that aligns with the goals of the granting corporation—such as fostering innovation, supporting community development, or advancing sustainability. The company must be a legally registered entity, like an LLC or corporation, as most grants are not open to individuals or informal operations. Applicants are usually expected to submit a detailed business plan or project proposal outlining how the funds will be used, projected outcomes, and how the initiative supports the company’s growth or community impact. Financial documentation is also commonly required, including tax records and income statements, to demonstrate fiscal responsibility and capacity to manage the grant. Additionally, some grants are limited based on business age, with eligibility restricted to either early-stage startups or more established companies. Many corporate grants also focus on specific industries or regions, so companies must often meet location or sector-related criteria. Lastly, businesses that emphasize innovation or measurable social impact—such as job creation, environmental sustainability, or equity—are often prioritized in the selection process. (Grant eligibility, n.d.)
    </p>
                             
    <u><b><p>References</u></b><br>
    <br>Weinger, A. (2025, January 17). What are corporate grants for nonprofits? Guide + examples. Double the Donation. <a href="https://doublethedonation.com/corporate-grants-for-nonprofits/">https://doublethedonation.com/corporate-grants-for-nonprofits/</a>
<br>
    <br>Huntsberger, A. (2025, April 10). The 4 Types of Grants for Nonprofits (2025). Neon One. <a href="https://neonone.com/resources/blog/grant-types-nonprofits/">https://neonone.com/resources/blog/grant-types-nonprofits/</a>
<br>
    <br>The shape of corporate philanthropy yesterday and today. (n.d.). Grantmakers in the Arts. <a href="https://www.giarts.org/article/shape-corporate-philanthropy-yesterday-and-today?">https://www.giarts.org/article/shape-corporate-philanthropy-yesterday-and-today?</a>
<br>
    <br>Dunn, B. (2023, November 20). The New Corporate Philanthropy - American Affairs Journal. American Affairs Journal. <a href="https://americanaffairsjournal.org/2023/11/the-new-corporate-philanthropy/?">https://americanaffairsjournal.org/2023/11/the-new-corporate-philanthropy/?</a>
<br>
    <br>Grants - Pros and Cons | Society for Nonprofits. (n.d.). <a href="https://www.snpo.org/funding/grants.php">https://www.snpo.org/funding/grants.php</a>
<br>
    <br>Grant eligibility | Grants.gov. (n.d.). <a href="https://www.grants.gov/learn-grants/grant-eligibility.html">https://www.grants.gov/learn-grants/grant-eligibility.html</a>
    </p>
    <p><b><u>Legal Qualification Requirements</u></b>
    	 Registered Business Entity – Must be legally formed (e.g., LLC, Corporation, Sole Proprietorship).
    	Valid Tax ID – Requires an EIN or TIN from a tax authority.
    	Good Standing Status – Must be current on taxes and regulatory filings.
    	Proper Licenses & Permits – Must hold all necessary business licenses to operate legally.
    	Financial & Legal Transparency – Should provide financial documents and disclose any legal issues.
    	Clean Legal History – No history of fraud, bankruptcy, or major legal violations.
    	Location Eligibility – Must be registered or operating in eligible regions, if geographically restricted.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>	Business Plan or Project Proposal
    <br>A detailed outline explaining your company’s mission, goals, operations, and how the grant funds will be used.
    <br>	Proof of Legal Business Status
    <br>Documents such as articles of incorporation, business registration certificate, or a business license.
    <br>	Tax Identification Number (EIN or TIN)
    <br>A copy of your federal Employer Identification Number issued by the IRS or equivalent.
    <br>	Financial Statements
    <br>Recent balance sheets, income statements, and cash flow statements—usually for the past 1–3 years.
    <br>	Tax Returns
    <br>Federal and/or state business tax returns to demonstrate financial history and compliance.
    <br>	Certificate of Good Standing
    <br>Issued by your Secretary of State or other business authority, confirming that your business is legally compliant and up to date.
    <br>	Organizational Chart or Team Bios
    <br>Information about your company’s leadership and staff, showing qualifications and experience.
    <br>	Bank Account Information or Void Check
    <br>For direct deposit of grant funds, if awarded.
    <br>	Proof of Location
    <br>Utility bills, lease agreements, or other documents confirming your business address (especially for location-specific grants).
    <br>	Letters of Support or References (if applicable)
    <br>Letters from community partners, customers, or stakeholders that support your grant application.
    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def grantscorporategrantsfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Grants<br>
    Capital Type: Corporate Grants</center></p>                        
    <p><center><u><b>List of AI Chatbot FAQs for Corporate Grants</u></b></center></p>
    <p><u><b>1. What are corporate grants?</u></b><br>
    • Answer: Corporate grants are non-repayable funds provided by companies (rather than governments or foundations) to support businesses, startups, or nonprofits that align with the company’s mission, values, or business goals. These grants may focus on innovation, community development, social impact, education, or diversity initiatives.
    </p>
                             
    <p><u><b>2. How are corporate grants different from loans or investments?</u></b><br>
    • Answer: Grants do not need to be repaid, and they do not require equity or ownership in your business. Loans must be repaid with interest, and investments require giving up a portion of ownership. Corporate grants are essentially gifts, although they often come with reporting requirements or expectations of impact.
    </p>
                             
    <p><u><b>3. Why do corporations offer grants?</u></b><br>
    • Answer: Corporations offer grants to:
    •	Support their Corporate Social Responsibility (CSR) goals
    •	Encourage innovation in areas that complement their business
    •	Invest in diverse founders, underrepresented groups, or local communities
    •	Promote positive brand image and public goodwill
    </p>
                             
    <p><u><b>4. Who can apply for corporate grants?</u></b><br>
    • Answer:Eligibility varies, but typical applicants include:
    •	Small businesses and startups
    •	Nonprofit organizations
    •	Entrepreneurs
    •	Minority-owned, women-owned, or veteran-owned businesses
    •	Businesses aligned with specific industries (e.g., tech, sustainability, education)
    </p>
                             
    <p><u><b>5. What types of projects do corporate grants support?</u></b><br>
    • Answer: Corporate grants may support:
    •	Product development or innovation
    •	Community outreach programs
    •	Sustainability or environmental initiatives
    •	Educational or workforce development programs
    •	Health and wellness projects
    •	Technology solutions
    </p>
                             
    <p><u><b>6. Do I have to be a customer of the company to receive a grant?</u></b><br>
    • Answer: Usually not, but some grant programs are restricted to existing customers or users of a company’s platform or services. Always check the eligibility requirements—some grants are open to the public, while others are by invitation or limited to specific groups.</p>
                             
    <p><u><b>7. What is typically required in a corporate grant application?</u></b><br>
    • Answer: A standard application may require:
    •	A detailed project or business proposal
    •	A budget or financial plan
    •	Background about your organization or team
    •	A description of expected impact or outcomes
    •	Supporting documents (like tax ID, registration, or business license)

    Some grants also ask for pitch videos, testimonials, or examples of past work.
    </p>
                             
    <p><u><b>8. Are corporate grants competitive?</u></b><br>
    • Answer: Yes. Corporate grants are highly competitive because they’re free money with no repayment or equity involved. The more prestigious or high-dollar the grant, the more applicants it typically attracts. A strong application that clearly aligns with the grant’s mission will stand out.</p>
                             
    <p><u><b>9. How much money can I receive through a corporate grant?</u></b><br>
    • Answer: Grant sizes vary widely. Some micro-grants may be as small as $500 to $5,000, while others may offer $10,000 to $100,000 or more. Occasionally, corporate challenges or innovation contests award grants of six figures or higher to select winners.</p>
                             
    <p><u><b>10. Are corporate grants only for U.S.-based businesses?</u></b><br>
    • Answer: Before tapping into your home equity, it’s worth considering other financing options like business loans, angel investors, venture capital, or crowdfunding. These options may carry less risk than using your home as collateral. It’s essential to weigh the pros and cons of each funding source before deciding.</p>
    
    <p><u><b>11. How long does it take to receive funds after winning a grant?</u></b><br>
    • Answer: It varies by program, but most corporate grants distribute funds within 4 to 12 weeks after the winners are announced. Some may be faster, especially for smaller amounts.</p>

    <p><u><b>12. What are my responsibilities after receiving a corporate grant?</u></b><br>
    <br>• Answer: Most grants come with basic expectations, such as:
    <br>• Progress reports or outcome summaries
    <br>• Use of funds for the approved purpose
    <br>• Public acknowledgment or branding (in some cases)
    <br>• Participation in publicity or case studies for the corporation
    <br>
    <br> Always read the terms and reporting requirements before accepting the grant.  
    </p>
        <p><u><b>13. Can I apply for more than one corporate grant at the same time?</u></b><br>
        <br>• Answer:Yes. You can apply to multiple grants, even from the same corporation, as long as there are no specific restrictions. Just make sure each application is tailored to the specific program.
    <br>
    <br> Always read the terms and reporting requirements before accepting the grant.  
    </p>
    <p><u><b>14. Where can I find corporate grants to apply for?</u></b><br>
    <br>• Answer: You can find them through:
    <br>•	The company’s official website (under “Social Impact,” “CSR,” or “Grants”)
    <br>•	Small business development centers
    <br>•	Nonprofit directories
    <br>•	Grant platforms like Hello Alice, Grants.gov, or IFundWomen
    <br>•	Startup accelerators or incubators that partner with corporations
    </p>
    <p><u><b>15. Are there strings attached to corporate grants?</u></b><br>
    <br>• Answer: Sometimes. While grants are generally “free money,” some come with conditions, such as promotional obligations, required participation in training or events, or usage restrictions. Always read the fine print before accepting funds.
    </p>    
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def grantscorporategrantstwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR</b></u><br>
    Capital Type: Corporate Grants</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    The ideal stage for seeking corporate grants is typically early to growth stage, where you’ve developed a product or MVP and have some initial traction or customers. Corporate grants are suited for businesses ready to grow but not yet fully scaled, as they aim to support ventures with potential. Startups in the idea phase or fully scaled businesses may not be ideal candidates for these grants.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    For corporate grants, the best entity types are generally LLCs, corporations (C-Corp or S-Corp), or nonprofits (501(c)(3)) because they show legitimacy and allow for clear financial reporting. Sole proprietors can apply, but may face more restrictions. Having a registered, compliant business entity increases your chances of qualifying for funding.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    Most corporate grants are best suited for companies with low to moderate pre-capital raised—typically $0 to $250,000. If you’ve raised small amounts, such as from friends and family or early revenue, it shows commitment and traction. However, large venture capital funding (over $1M) might make you less eligible, as grants target companies in the early stages of growth.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    Seed or early-stage funding, typically from angel investors, family, or small VC rounds, is the best type of capital to have raised before applying for a corporate grant. This stage shows your company has validation and is progressing but still needs funding for growth. It demonstrates credibility without being overly reliant on institutional investors.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    Corporate grants typically range from $5,000 to $100,000, with smaller grants usually supporting specific projects like product development or market research. Larger grants tend to be for significant initiatives with higher growth potential or social impact. Be sure to check grant details to understand the funding limits and eligible uses.
    </p>
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Seed and Series A rounds are the best stages to apply for corporate grants. At Seed, you’re still in early development, while by Series A, you’ve validated your business model and may be looking to scale. Corporate grants can support specific initiatives, like product innovation or expansion, at these stages.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    The best number of capital rounds for applying is typically one to two, usually Seed or Series A. These rounds show progress without full institutional backing, making your company an attractive candidate for grants. By Series A, you’ve demonstrated your potential but still require non-dilutive funding.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Corporate grants are best used for projects that align with the corporation’s goals, such as product development, sustainability efforts, or community outreach. These funds should be used for measurable initiatives that create impact, whether in expanding your product line or addressing social issues like DEI (diversity, equity, and inclusion).
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    The risk level of corporate grants is low compared to other funding types, as they are non-dilutive and non-repayable. However, there are risks such as stiff competition, the potential for not being awarded the grant, and the need to comply with specific usage terms. There’s also the risk of dedicating significant time to the application process without success.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The cost of capital for corporate grants is typically zero, as grants are non-dilutive and non-repayable. However, indirect costs include the time and effort spent on preparing the application, as well as potential fees for grant writers or legal assistance. These should be factored into your overall planning.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    The upfront costs for corporate grants are generally low and mostly involve time spent on applications. If you hire professional help, like a grant writer, fees can range from $1,000 to $5,000 depending on the grant’s complexity. Legal or administrative costs for compliance may also be part of the upfront expenses.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    The typical timeframe for receiving a corporate grant range from one to six months. The process involves application submission, review, evaluation, and potential funding disbursement. The length depends on the grant cycle and evaluation period, with some programs offering faster results and others having more extended timelines.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)