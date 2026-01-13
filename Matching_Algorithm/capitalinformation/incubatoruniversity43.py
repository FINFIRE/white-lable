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


def incubatoruniversity(request):
    introduction = mark_safe("""<p><b><center><u>Definition of Capital Market: Incubator</u></b>
    <br>Capital Type: University</center></p>
                             
    <p><b><u>Introduction</u></b></p>
    <p>Studies show that university incubators can increase the likelihood of startup success by 60%, as they provide access to research, technology, and an eager talent pool <a href="https://www.spectup.com/resource-hub/startup-incubators">(source)</a>.Startups in these programs report a 70% survival rate after five years—much higher than their peers <a href="https://www.spectup.com/resource-hub/startup-business-incubators">(source)</a>.</p>

    <p><b><u>Definition of Capital Type</u></b></p>
    <p>1) Incubators focus on startups that don’t necessarily have a business plan or model in place. Services provided by incubators include office space, administrative functions, education and mentorship, access to investors and capital, and idea generation. Incubators either charge a fee for their service or take an equity stake in the startup. The period of incubation can last from a few months to several years. Incubators focus on companies that are just starting to develop their idea into a business while accelerators take startups with an established business model and accelerate their time to market. (Smith, 2021)</p>

    <p>2) Business incubators within the university environment augment teaching and learning with real-world engagement and the advancing of an idea and knowledge-rich network. Incubators provide a route for students, and staff, to create new ventures and develop both the business and themselves. As a hub of creativity and innovation, incubators also become a space of trust and collegiality, as the hopes and fears of individuals or groups are shared.</p>

    <p>Incubators are all-embracing and should maintain an ‘open door policy’ that invites all businesses to collaborate and share both knowledge and experience. With this in mind, these spaces assist individuals and groups in many ways, including critiquing an idea, establishing a market for the product or service, and building these valuable networks. (Crammond, 2023)</p>

    <p>3) Not all university-based business incubators are the same. Some, like the NYU Startup Accelerator, are open only to teams that include students enrolled at the host institution. They help transition their early-stage entrepreneurs from discovery to innovation. Others, like DMZ at Ryerson University, are not just for student entrepreneurs. DMZ accelerates businesses at multiple stages. This is also the case with Stanford University's StartX. There are also for-profit university-based models — such as University of California, Berkley’s SkyDeck — that invest capital into startups — and sector-agnostic models, like Yale University's InnovateHealth, that support ventures in a variety of industries. (Snobar, 2019)</p>

    <p>4) A sizable selling point of university-based incubators is the freedom for early-stage testing and experimentation. Before startups become startups, products must be designed, development methods must be established, team dynamics need to be organized, and workflows adjusted. University incubators provide a longer runway to build a startup before student entrepreneurs enter into a competitive market and grapple with life’s constraints post-graduation.</p>

    <p>On top of a fertile innovation space, some university incubators enhance their offerings with seed funding and or access to Alumni investors and connected venture capital firms. The investor collaboration and the additional seed funding save would-be-entrepreneurs time courting investors. And at the same time, investors can leverage university incubators as vetting tools for prospective startup investments.</p>

    <p>For the savvy startup, universities offer an embarrassment of riches. They have business schools staffed with professors specializing in finance, accounting, marketing, operations, and business management. There are clubs and associations for collaboration and feedback. Opportunities to harness volunteer support. Seasoned faculty carrying years of R&D experience in an array of industries and fields.</p>

    <p>With all the classes, curriculums, and equipment, universities essentially enable entrepreneurs to scale faster, plan more effectively, and design more efficiently and affordably than they would on their own. And though it’s true university incubators don’t house every university resource, startups don’t grow in a vacuum either. Depending on the focus, a student entrepreneur can take advantage of any number of resources while on campus. (University Incubators Present New Growth Opportunities for Startups, n.d.)</p>

    <p><b><u>References</u></b></p>
    <p>Baxter, J. (2023, October 20). Innovation meets entrepreneurship: The value of academic incubators. Retrieved from University Business: <a href="https://universitybusiness.com/innovation-meets-entrepreneurship-the-value-of-academic-incubators/">https://universitybusiness.com/innovation-meets-entrepreneurship-the-value-of-academic-incubators/</a></p>

    <p>Crammond, D. R. (2023, October 11). The importance of university-based incubators and evidencing PSF-relevant enterprising attributes. Retrieved from Advanced HE: <a href="https://www.advance-he.ac.uk/news-and-views/importance-university-based-incubators-and-evidencing-psf-relevant-enterprising">https://www.advance-he.ac.uk/news-and-views/importance-university-based-incubators-and-evidencing-psf-relevant-enterprising</a></p>

    <p>Smith, T. D. (2021). Business Capital 101. San Francisco: Imaginary Press.</p>

    <p>Snobar, A. (2019, July 9). College And University Incubators Should Start Practicing What They Preach. Retrieved from Forbes: <a href="https://www.forbes.com/councils/forbestechcouncil/2019/07/09/college-and-university-incubators-should-start-practicing-what-they-preach/">https://www.forbes.com/councils/forbestechcouncil/2019/07/09/college-and-university-incubators-should-start-practicing-what-they-preach/</a></p>

    <p>University Incubators Present New Growth Opportunities for Startups. (n.d.). Retrieved from Emory University : <a href="https://hatchery.emory.edu/articles/university-incubators.html">https://hatchery.emory.edu/articles/university-incubators.html</a></p>

    <p><b><u>Legal Qualification Requirements</u></b></p>
    <p>• Business Structure – Must be a for-profit entity, typically a corporation (C-Corp or S-Corp) or LLC.<br>• Location and Affiliation – Must be affiliated with the university or based in the program’s designated region.<br>• Stage of Development – Typically requires early-stage businesses with a proof of concept or prototype.<br>• Intellectual Property (IP) – Must own or have rights to any intellectual property; some incubators may require IP developed with university resources to be shared.<br>• Equity and Investment Terms – Be prepared to offer equity (usually 5%-10%) in exchange for resources and funding.<br>• Legal Compliance – The business must be in good legal standing, with all necessary licenses and compliance with applicable laws.<br>• Pre-existing Funding – Some incubators may limit the amount of capital already raised and prefer businesses in the pre-seed or seed stage.<br>• Team Composition – Must have a qualified management team; some incubators may prioritize businesses with university-affiliated founders or teams.<br>• Industry Focus – Some incubators specialize in certain industries like tech, biotech, or social impact.<br>• Application Requirements – Must submit a business plan, financials, and other legal or financial disclosures as part of the application process.</p>

    <p><b><u>Supporting Document List</u></b></p>
    <p>• Business Plan – A comprehensive document outlining the company’s mission, vision, target market, business model, competitive landscape, and financial projections.<br>• Pitch Deck – A visual presentation (usually around 10-15 slides) summarizing the business idea, the team, market opportunity, product or service, and funding needs.<br>• Financial Statements – Includes balance sheets, income statements, and cash flow statements (if applicable), providing a snapshot of the company’s financial health.<br>• Projections and Forecasts – Financial projections for the next 3-5 years, outlining expected revenues, costs, profit margins, and growth plans<br>• Founders and Team Information – Documentation about the founders and key team members, including resumes, bios, and relevant experience or qualifications.<br>• Ownership and Equity Structure – A breakdown of the company’s ownership structure, including shareholder agreements, stock options, and equity distribution.<br>• Intellectual Property (IP) Documentation – Proof of ownership or rights to any intellectual property, such as patents, trademarks, copyrights, and any licenses associated with IP.<br>• Legal Compliance Documents – Copies of business registration documents, tax identification numbers, and any relevant licenses or permits required for the business to operate.<br>• Incorporation Documents – Articles of incorporation or operating agreements that outline the legal formation of the business entity (C-Corp, LLC, etc.).<br>• Cap Table (Capitalization Table) – A detailed breakdown of the company’s equity ownership, including shares, options, and any convertible securities.<br>• Investor or Funding History – Information on any previous investments, including details about prior funding rounds, investors, and the terms of those investments.<br>• Non-Disclosure Agreement (NDA) – If required, a confidentiality agreement to protect proprietary information shared with the incubator during the application process.<br>• Market Research and Analysis – Data and insights about the target market, including customer demographics, competitive analysis, and industry trends.<br>• Product/Service Demonstrations or Prototypes – Documentation or working models demonstrating the company’s product or service, including any user feedback or early customer testimonials.<br>• Application Forms – Specific forms required by the incubator for applying to their program, which may include basic company information, founder details, and program eligibility criteria.</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def incubatoruniversityfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Incubator<br>
    Capital Type: University</center></p>                        
    <p><center><u><b>Frequently Asked Question for University Incubator</u></b></center></p>
    
    <p><b><u>1. What exactly is a university incubator?</u></b><br> 
    A university incubator is a program offered by universities to support startups and early-stage companies, often focusing on technology or research-based ventures. It typically provides access to resources such as mentorship, office space, funding opportunities, networking, and sometimes even direct investment from university-backed funds.</p>

    <p><b><u>2. What are the main benefits of using a university incubator to raise capital?</u></b><br> 
    • Access to Academic Resources: Collaborations with university researchers, labs, and intellectual property can help validate and enhance your business idea.<br>
    • Mentorship and Expertise: Access to university-affiliated mentors, professors, and industry experts who can guide the company’s development and business strategy.<br>
    • Networking Opportunities: Connection to a network of investors, alumni, and partners tied to the university ecosystem.<br>
    • Flexible Funding Options: Some incubators may offer seed funding or facilitate introductions to angel investors and venture capitalists.<br>
    • Credibility: Being associated with a respected academic institution can increase your company’s credibility with investors, partners, and customers.</p>

    <p><b><u>3. How does a university incubator differ from other types of incubators or accelerators?</u></b><br> 
    Unlike private or corporate incubators, university incubators often focus more on innovation driven by academic research and may offer more flexible terms. The university’s involvement might provide better access to intellectual property (IP), research funding, and potential for long-term strategic partnerships. They also may have a stronger emphasis on nurturing early-stage, research-driven companies rather than purely commercial ventures.</p>

    <p><b><u>4. How do university incubators fund startups?</u></b><br> 
    • Seed funding: Some incubators provide initial seed funding either through university-backed grants or their own funds.<br>
    • Investor introductions: Incubators may not directly provide funding but can connect you with venture capitalists, angel investors, or other funding sources within their network.<br>
    • Equity-based support: In exchange for resources and funding, university incubators may require equity in your company. The exact terms vary.</p>

    <p><b><u>5. What are the costs associated with joining a university incubator?</u></b><br> 
    • Equity share: Many incubators ask for an equity stake in your company, typically between 5%-10%.<br>
    • Fees: Some incubators charge nominal fees for office space, access to labs, or administrative support, though many university-based programs are subsidized.<br>
    • Commitment to university resources: Your company may need to allocate a certain amount of time or resources to collaborate with the university on projects or research.</p>

    <p><b><u>6. What types of companies are university incubators best suited for?</u></b><br> 
    University incubators are ideal for companies in industries that are research-driven or rely on deep technical expertise, such as:<br>
    • Biotech and life sciences<br>
    • Clean energy and environmental technologies<br>
    • Advanced manufacturing and engineering<br>
    • Artificial intelligence and machine learning<br>
    • Software development, particularly in research-heavy fields<br>
    • If your startup involves heavy innovation, patents, or academic collaboration, a university incubator could be a strong fit.</p>

    <p><b><u>7. How long can I expect to stay in a university incubator?</u></b><br> 
    • Program duration: Incubator programs typically last anywhere from six months to two years, depending on the structure. Some offer rolling participation, while others have set intake periods.<br>
    • Post-program support: Many incubators offer alumni services or continued access to their resources after you leave the formal program, allowing your company to remain within their network for the long term.</p>

    <p><b><u>8. What support services do university incubators provide beyond funding?</u></b><br> 
    • Mentorship and advisory boards: Access to experienced advisors, including professors, successful entrepreneurs, and business professionals.<br>
    • Networking events: Opportunities to meet potential customers, partners, investors, and other entrepreneurs.<br>
    • Legal and IP assistance: Help with patent filing, trademarks, and navigating the complexities of IP in a research-based startup.<br>
    • Marketing and business development: Assistance with business plans, pitching to investors, and expanding your market reach.<br>
    • Physical infrastructure: Office space, labs, and access to university facilities.</p>

    <p><b><u>9. Do I need to have university-affiliated founders to join an incubator?</u></b><br> 
    Not necessarily. While some university incubators may prioritize startups founded by current students, alumni, or faculty members, many are open to external entrepreneurs as long as there is a strong alignment with the university’s research goals or innovation focus.</p>

    <p><b><u>10. What is the selection process for joining a university incubator?</u></b><br> 
    • Application: Most incubators have a competitive application process that requires a detailed business plan, pitch, and often, a demonstration of the innovation or technology behind your business.<br>
    • Interview/pitch: Selected applicants are usually invited to pitch their business to a panel of mentors and potential investors.<br>
    • Due diligence: The university will assess the team, business model, market potential, and alignment with its innovation and research priorities.</p>

    <p><b><u>11. How do university incubators help with intellectual property (IP) management?</u></b><br> 
    University incubators often have strong legal and IP teams that assist with:<br>
    • Patent protection: Help with filing patents for new technologies or innovations developed within the incubator.<br>
    • IP licensing: Support for licensing agreements that could open up additional revenue streams or commercial partnerships.<br>
    • Ownership structure: They may help clarify IP ownership between the university, entrepreneurs, and investors, ensuring that rights are properly assigned.</p>

    <p><b><u>12. What’s the downside or risk of using a university incubator?</u></b><br> 
    • Equity dilution: If you’re accepting funding or support, you may need to give up equity in exchange for resources or financial backing.<br>
    • Limited flexibility: University incubators may have certain restrictions or guidelines related to working within the university’s ecosystem that could impact your business decisions.<br>
    • Lengthy timelines: The research-driven nature of many university incubators could mean longer development cycles, which might not align with startups that need faster growth.</p>

    <p><b><u>13. How do I evaluate whether a university incubator is the right option for my startup?</u></b><br> 
    • Match with university strengths: Consider if your business aligns with the university’s research focus or technological expertise.<br>
    • Assess resources: Evaluate the mentorship, funding, infrastructure, and networking opportunities the incubator offers.<br>
    • Examine track record: Research the success stories of past incubator graduates to understand how well the program has supported similar companies.<br>
    • Look at the financial terms: Be clear about equity requirements, fees, and any other commitments that might affect your business’s ownership or growth potential.</p>
    """)

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def incubatoruniversitytwelve(request):
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
    University Incubator</center>

    <p><b><u>1 - Stage of Development Assessment</u></b><br>
    The ideal stage for a company to enter a university incubator is typically the idea or formation stage, where they can access research, mentorship, and infrastructure to develop their idea and prototype. However, university incubators can support startups throughout the early stages of their development, especially if they need ongoing guidance or funding assistance.</p>

    <p><b><u>2 - Entity Type Assessment</u></b><br>
    The ideal entity type for a business to use a university incubator depends on a few factors such as the company's stage of development, the nature of its business, and its goals for growth. Early-stage startups looking for flexibility and lower administrative complexity often choose an LLC. If the goal is to attract venture capital or grow quickly, a C Corporation is typically the ideal entity type. Nonprofits may be suitable for businesses focused on social impact or research collaborations with universities.</p>

    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    University incubators generally do not have strict restrictions regarding businesses that have raised a certain amount of pre-capital before entering the program. If a business has raised considerable funding, it may want to consider other programs, such as accelerators or growth-stage incubators, that cater to companies that have already secured funding and are looking for more advanced support.</p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    While there are generally no blanket restrictions based on how capital was raised, the nature of the funding (whether it’s venture capital, angel investment, government grants, crowdfunding, etc.) could affect whether a company is eligible or well-suited for a particular university incubator. The incubator's goals and focus (e.g., early-stage research commercialization, venture capital readiness, or social impact) will determine if a business that has raised a certain amount of capital is considered a good fit.</p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    The amount a company can raise using a university incubator varies significantly based on several factors, including the type of incubator, the stage of the company, and the resources available. Here's a general range:<br>
    Non-dilutive funding: A few thousand to a few hundred thousand dollars (typically in the form of grants or prizes).<br>
    Seed funding (direct from incubator or investors): $10,000 to $100,000 or more, depending on the incubator’s investment model and connections.<br>
    Venture capital or angel investment: University incubators can help companies connect to investors who might provide hundreds of thousands to millions of dollars in funding as the company scales.<br>
    The most significant value university incubators provide is often access to a network of investors, research facilities, and mentorship, helping businesses grow and raise larger funding rounds through external sources.</p>

    <p><b><u>6 - Capital Round Assessment</u></b><br>
    Pre-seed and seed stages are the best fits for startups entering university incubators, as these programs are designed to support businesses at the early development phase and help them secure initial funding, build their products, and refine their business models before scaling to larger capital rounds.</p>

    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    There is no fixed rule about how many tranches are ideal when raising capital using a university incubator, but typically, two to three tranches are common for a company moving from early-stage development to scaling and preparing for larger rounds of investment. The number of tranches depends on the company’s progress, the incubator’s resources, and the capital needs of the startup.</p>

    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    While university incubators offer valuable financial support, they often impose restrictions to ensure that the funds are used effectively for business development and growth. These restrictions generally focus on ensuring that the funds are spent on the startup’s core activities, like research, product development, and market validation, and not on personal expenses or unrelated investments. Startups must work within these guidelines and often need to provide clear budgets, milestones, and accountability to ensure compliance with the terms of funding.</p>

    <p><b><u>9 - Risk Assessment</u></b><br>
    A business looking to use a university incubator needs a moderate to high risk tolerance. This involves accepting the uncertainty of early-stage development, working within structured environments, and understanding that failure is a possibility. However, university incubators also provide substantial support through funding, mentorship, and resources, which can help mitigate some risks.</p>

    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    A business using a university incubator should have a moderate to moderate capital cost tolerance. It needs to be prepared for possible equity dilution, up-front and ongoing operational costs, legal and compliance expenses, and the costs associated with research and development, marketing, and scaling.</p>

    <p><b><u>11 - Up Front Cost Assessment</u></b><br>
    The upfront costs for a company to enter a university incubator can range from a low estimate of $1,500 to $5,000 for smaller or low-cost incubators, to higher costs up to $10,000 to $30,000 in cases where additional fees, legal costs, or specialized R&D expenses are involved.</p>

    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
    The speed at which a business can secure capital through a university incubator varies, but companies can typically access initial funding or grants within 3–6 months of entering the program. If external investment is sought (such as venture capital or angel funding), it may take between 6–12 months depending on the company's progress and the incubator's network.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)