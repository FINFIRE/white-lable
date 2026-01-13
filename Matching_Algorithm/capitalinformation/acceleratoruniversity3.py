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


def acceleratoruniversity(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Accelerator</b></u><br>
    Capital Type: University</center></p>
    
    <p><b><u>Introduction</u></b><br>
    Research published in 2024 found that startups that went through an accelerator raised 50% to 170% more from investors than did similar startups that applied but were not accepted into the same accelerators <a href="https://crsreports.congress.gov/product/pdf/IF/IF12794/2">(source)</a>. According to research, the global startup accelerator market was valued at $1.15 billion in 2020 and is projected to reach $2.55 billion by 2027. <a href="https://www.linkedin.com/pulse/startup-accelerator-market-size-2024-analysis-dguye/">(source)</a>

    <br><br>Accelerator graduates that went on to raise additional venture capital investment had a median valuation of $15.6 million during this period, and an average valuation of $90 million <a href="https://hbr.org/2016/03/what-startup-accelerators-really-do">(source)</a>.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    1) Entrepreneurial universities have broadened their scope, serving as a platform for collaboration, creation, and dissemination of knowledge through the orchestration of multi-stakeholder partnerships and networks involving public and private organizations. This sometimes culminates in the creation of university-based accelerators (UBAs), i.e., new organizations specifically designed to support entrepreneurial action, growth, and survival of new ventures within the ecosystem.

    <br><br>UBAs are accelerators founded and supported by a university. They act as vehicles to facilitate intrapreneurship within entrepreneurial universities and have the twofold objective of supporting the transition of ideas from the lab to the market and fostering entrepreneurial skills among students. Like traditional accelerators, they typically offer entrepreneurship-related training programs over a fixed and short period (three to nine months) and provide services like office space, mentorship, coaching, and advisory by leveraging the resources and network of the university. Sometimes, they also invest in the accelerated startups, which are subject to a strict selection process. (Monica Masucci, 2024)

    <br><br>2) The biggest challenge encountered by universities in their efforts to commercialize important new discoveries is the technology development gap: the void that exists between early-stage inventions and the stage innovative technologies must reach in order to be viable and attractive candidates for licensing and commercialization.

    <br><br>Accelerator programs combine funding strategies, technical support, and business expertise to help promising innovations make the leap from the lab to the commercial sphere and focuses on forging new partnerships for the greatest societal impact. (Bridging the development gap, n.d.)

    <br><br>3) “Participation in these programs is a strategic decision not only for entrepreneurs, but also investors and other ecosystem participants,” notes Fehder, a PhD candidate at the MIT Sloan School.

    <br><br>In his research, Fehder uses data from the Boston-based MassChallenge startup accelerator—founded by John Harthorne MBA ’07 in 2010—to more accurately measure the effect such programs exert on companies. He also examines the change in entrepreneurial activity that occurs when an accelerator arrives in a specific region. “Accelerators, and other programs like them, provide an opportunity to observe the dynamics that shape entrepreneurship systems,” he explains. (Who Benefits Most from Business Accelerators?, 2016)

    <br><br>4) (University) Accelerated startups were 3.4% more likely to raise venture capital and raised $1.8 million more in the first year after graduating from these programs,” Assenova said. “They also planned to raise $2.64 million more capital, on average, over the next year. Accelerated startups also generated more revenue, hired more full-time employees, and paid more in wages to their employees, on average — indicating that they were scaling faster than their peers.” (Murray, 2024)

   <br><br> 5) Universities have an innate knack for discovery. Their professors regularly pen leading research, their scientific breakthroughs have revolutionized industries, and their contributions to health and medicine have literally halted epidemics and saved lives. Against this backdrop, it seems only natural that colleges and universities would make for excellent startup accelerators.

    <br><br>Academia shares the entrepreneurial ambition for discovery and innovation. That focus benefits from unique and often unmatched resources in academic expertise, networking, access to potential funding sources, and industry tools to jumpstart new—and potentially unorthodox—ventures. (University Incubators Present New Growth Opportunities for Startups, n.d.)
    </p>
                             
    <u><b><p>References</u></b><br>
    Bridging the development gap. (n.d.). Retrieved from Harvard: <a href="https://otd.harvard.edu/accelerators/">https://otd.harvard.edu/accelerators/</a>
    <br><br>Monica Masucci, R. C. (2024, August). How do accelerators emerge and develop in entrepreneurial universities? Retrieved from Science Direct : <a href="https://www.sciencedirect.com/science/article/pii/S0166497224001032">https://www.sciencedirect.com/science/article/pii/S0166497224001032</a>
    <br><br>Murray, S. (2024, May 7). Do Accelerators Improve Startup Success Rates? Retrieved from University of Pennsylvania: <a href="https://knowledge.wharton.upenn.edu/article/do-accelerators-improve-startup-success-rates/">https://knowledge.wharton.upenn.edu/article/do-accelerators-improve-startup-success-rates/</a>
    <br><br>University Incubators Present New Growth Opportunities for Startups. (n.d.). Retrieved from hatchery.emory.edu: <a href="https://hatchery.emory.edu/articles/university-incubators.html">https://hatchery.emory.edu/articles/university-incubators.html</a>
    <br><br>Who Benefits Most from Business Accelerators? (2016, April). Retrieved from Better World MIT: <a href="https://betterworld.mit.edu/benefits-business-accelerators/">https://betterworld.mit.edu/benefits-business-accelerators/</a>
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>• Legal Entity Status – Must be a legally registered entity (e.g., corporation or LLC) with formal recognition under local laws. 
    <br>• Jurisdictional Eligibility – Must be incorporated and operating in the accelerator’s permitted region, with some programs having geographic restrictions.
    <br>• Industry Eligibility – The business should align with the accelerator's focus area (e.g., tech, healthcare, fintech). Some accelerators specialize in specific industries.
    <br>• Founder and Ownership Requirements – Founders must have a significant ownership stake (e.g., at least 50%) and be actively involved in the business operations.
    <br>• Business Stage and Revenue Requirements – Accelerators generally target early-stage startups (e.g., pre-seed or seed stage) with little to moderate revenue, and may have revenue limits.
    <br>• Intellectual Property (IP) Considerations – The business must either own or have legal rights to key intellectual property (e.g., patents, proprietary technology), and IP should be protected.
    <br>• Founder and Executive Team Background Checks – Founders and key team members may undergo background checks for any legal or regulatory issues, especially regarding criminal history.
    <br>• Compliance with Securities Regulations – Must comply with securities laws when offering equity or debt to investors, often using vehicles like SAFE or convertible notes.
    <br>• Commitment to Program Requirements – Must sign an agreement to participate and meet specific program milestones, including fundraising events and equity exchange.
    <br>• Eligibility for Government or University Grants – For some accelerators with grant funding, businesses may need to meet specific government or academic criteria to qualify.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Business Registration Documents – Must provide proof of legal entity status (e.g., Articles of Incorporation or Certificate of Formation) and any other registration certificates required by local jurisdiction.
    <br>• Business Plan or Pitch Deck – A comprehensive business plan or a pitch deck outlining the company's vision, market opportunity, growth strategy, and financial projections.
    <br>• Founder/Executive Team Bios and Background Information – Resumes/CVs or LinkedIn profiles for the founders and key executives, including professional background and relevant experience.
    <br>• Financial Statements – Must include balance sheet, income statement, and cash flow statement for the business, as well as financial projections for the next 3-5 years.
    <br>• Intellectual Property (IP) Documentation – Provide evidence of ownership or legal rights to intellectual property, such as patents, trademarks, or IP assignment agreements.
    <br>• Cap Table (Capitalization Table) – A document showing the ownership structure of the company, including shares, stock options, and convertible securities.
    <br>• Articles of Agreement or Operating Agreement – For corporations, Articles of Incorporation or Bylaws; for LLCs, an Operating Agreement outlining management structure and ownership.
    <br>• Investor and Funding Documentation – Provide records of prior funding rounds, including SAFE or convertible notes, investment agreements, and proof of funding from previous investors.
    <br>• Legal Compliance and Regulatory Documents – Documents proving compliance with relevant legal and regulatory requirements, including securities filings, licenses, and permits.
    <br>• University and Accelerator-Specific Forms – Any application forms, participation agreements, and non-disclosure agreements (NDAs) required by the accelerator program.
    <br>• Product or Service Documentation – Provide product demos, prototypes, market research, or customer testimonials supporting the viability of the business offering.
    <br>• Customer and Market Validation Materials – Evidence of market interest, such as customer contracts, letters of intent (LOIs), or sales and marketing materials.
    <br>• Tax and Compliance Documentation – Tax returns from previous years, sales tax permits, and other relevant tax documentation to ensure compliance with tax regulations.
    </p>
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def acceleratoruniversityfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Accelerator<br>
    Capital Type: University</center></p>                        
    <p><center><u><b>Frequently Asked Question for Accelerator-University</u></b></center></p>
    <p><u><b>1. What is a university accelerator, and how does it work?</u></b><br>
    • Answer: A university accelerator is a program offered by universities to support startups through funding, mentoring, and access to academic resources. These programs typically last a few months and provide early-stage companies with seed funding, office space, and exposure to a network of investors and professionals.
    </p>
                             
    <p><u><b>2. What are the benefits of using a university accelerator compared to other fundraising options?</u></b><br>
    • Answer: University accelerators offer several unique benefits, including:
    <br>- Access to academic expertise from faculty and researchers.
    <br>- Networking opportunities with alumni, industry leaders, and potential investors.
    <br>- In-kind support, such as office space, lab facilities, and technical resources.
    <br>- Mentorship from experienced entrepreneurs, faculty members, and business advisors.
    <br>- Seed funding or early-stage capital, often with more favorable terms than venture capital or angel investors.
    </p>
                             
    <p><u><b>3. What types of companies are best suited for a university accelerator program?</u></b><br>
    • Answer: University accelerators generally focus on early-stage companies, especially those in sectors aligned with the university’s strengths. This might include:
    <br>- Tech startups (e.g., software, AI, biotech)
    <br>- Healthcare innovations
    <br>- Social enterprises
    <br>- Engineering or product-based companies
    <br>- Research-driven startups that benefit from academic collaborations
    <br>- Startups that need support with product development, research, or access to scientific resources are particularly well-suited for these programs.</p>
                             
    <p><u><b>4. What is the funding structure provided by university accelerators?</u></b><br>
    • Answer: Funding provided by university accelerators often comes in the form of:

    <br>- Seed capital, typically between $25,000 to $250,000.
    <br>- Equity exchange, with universities typically taking a small equity stake (usually 5-10%) in return for the funding and support.
    <br>- Grants or non-equity funding may be available for specific projects, particularly in tech, health, or research.
    <br>- This funding model can be more flexible than venture capital or angel investments, with less stringent terms.</p>
                             
    <p><u><b>5. How much equity do universities take in exchange for accelerator participation?</u></b><br>
    • Answer: Typically, universities take an equity stake between 5% to 10% in exchange for their support. This is often lower than what investors may ask for in early-stage rounds, making it an attractive option for startups looking for capital without giving up too much control.
    </p>
                             
    <p><u><b>6. What kind of mentorship and support can I expect from a university accelerator?</u></b><br>
    • Answer: University accelerators provide a wide range of mentorship, including:
    <br>- Expert advisors from academia and industry.
    <br>- Entrepreneur-in-residence programs where seasoned entrepreneurs help guide you.
    <br>- Business development support to help scale your company.
    <br>- Technical guidance, particularly in fields like engineering, life sciences, and software development.
    <br>- Legal and financial advice, including assistance with business structures, patents, and fundraising.</p>
                             
    <p><u><b>7. Can university accelerators help me connect with investors?</u></b><br>
    • Answer: Yes, university accelerators are often connected to a network of investors, including venture capitalists, angel investors, and corporate partners who are actively looking for startups to invest in. The accelerator program may also host demo days, pitch competitions, and investor meetups to help you secure additional funding.</p>
                             
    <p><u><b>8. How do university accelerators compare to traditional venture capital or angel investors?</u></b><br>
    • Answer: University accelerators generally provide more early-stage, flexible capital with fewer strings attached compared to traditional venture capital or angel investors. Additionally, accelerators offer mentorship and access to resources that can be difficult to find in early fundraising rounds. Unlike traditional investors, accelerators often focus on the long-term growth and development of your company and may offer more favorable terms (e.g., lower equity stakes, non-equity funding).</p>
                             
    <p><u><b>9. What are the drawbacks or challenges of using a university accelerator?</u></b><br>
    • Answer: While university accelerators offer many benefits, there are potential drawbacks:
    <br>- Limited funding compared to venture capital, which could restrict the growth of your business.
    <br>- Equity dilution—while typically lower, giving up equity in the early stages can still be a concern for some entrepreneurs.
    <br>- Program duration—accelerators usually last only a few months, which may not be enough to get through all stages of product development or growth.
    <br>- Focus on academic alignment—the accelerator may be more suited to companies in specific industries or sectors that align with the university’s research strengths.</p>
                             
    <p><u><b>10. What other resources do university accelerators provide aside from funding?</u></b><br>
    • Answer: University accelerators provide more than just funding:
    <br>- Access to research facilities and lab space for product testing and development.
    <br>- Partnership opportunities with faculty members or university-affiliated research centers.
    <br>- Networking events, workshops, and seminars on entrepreneurship, marketing, and scaling a business.
    <br>- Pro bono legal and accounting services to help navigate the complexities of business formation and fundraising.</p>
                             
    <p><u><b>11. What is the application process for a university accelerator?</u></b><br>
    • Answer: The application process usually includes:
    <br>- Submitting a business plan or pitch deck, detailing your startup’s value proposition, team, market opportunity, and financial projections.
    <br>- Interviews or pitch sessions to assess your business's potential, the team’s capabilities, and fit with the accelerator’s offerings.
    <br>- Selection criteria may include the scalability of your business, the alignment with the 
    <br>- university's areas of expertise, and the innovation behind your product or service.</p>
                             
    <p><u><b>12. How long does a university accelerator program last?</u></b><br>
    • Answer: Accelerator programs generally last between 3 to 6 months, depending on the university. During this time, you’ll receive mentorship, access to resources, and opportunities to refine your business model and pitch for investors.
    </p> 
                             
    <p><u><b>13. Can I participate in a university accelerator if my company is not located near the university?</u></b><br>
    • Answer: Some university accelerators offer remote participation or hybrid models that allow companies from outside the university’s geographic area to participate. However, in-person participation may still be preferred for networking and taking full advantage of available resources.</p>

    <p><u><b>14. What happens after completing a university accelerator program?</u></b><br>
    • Answer: After completing the accelerator, you will likely:
    <br>- Have a stronger, more polished business plan and a clearer growth strategy.
    <br>- Be prepared to raise additional capital from investors, as the accelerator will have helped you build relationships with key stakeholders.
    <br>- Gain access to a growing network of alumni and partners who can continue to support your growth.</p>
    
     <p><u><b>15. How do I evaluate whether a university accelerator is the right fit for my business?</u></b><br>
    • Answer:  Evaluate the following:
    <br>- Alignment with your industry and goals—Does the accelerator have expertise and resources that will support your specific business needs?
    <br>- The strength of its network—Are there enough relevant mentors, investors, and partners who can help you scale?
    <br>- Funding terms—Are the terms (equity, funding amount, etc.) acceptable and favorable for your stage of growth?
    <br>- Reputation and success stories—Has the accelerator helped other startups succeed, and does it have a strong track record?</p>           
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def acceleratoruniversitytwelve(request):
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
    Capital Type: University Accelerator</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    While university accelerators tend to favor early-stage companies, they also provide mentorship, networking, and research resources that help bridge the gap between the idea stage and scaling. This makes them a great fit for companies that need academic resources and mentoring to take the next step towards product development and market entry.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    The ideal entity type for a business entering a university accelerator is generally either an LLC or a C-Corp, with C-Corps being the most common choice for businesses aiming for scalability, venture capital investment, and growth. University accelerators usually prefer these entities because they are legally established, have clear ownership structures, and are better suited for future funding rounds. The choice between LLC and Corporation depends on the specific needs and goals of the startup.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    While many university accelerators are focused on early-stage startups with limited pre-existing capital, there are typically no restrictions regarding the amount of funding a business has already raised.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    While most university accelerators are primarily concerned with the stage of the company rather than the exact method of raising capital, the nature and complexity of pre-existing funding can sometimes interfere with accelerator participation. Factors such as equity dilution, investor relationships, terms of previous funding rounds, and intellectual property restrictions may affect how a company can engage with the accelerator. 
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    The amount a company can raise using a university accelerator is typically seed funding in the range of $25,000 to $250,000, but it can be higher for more specialized or research-focused accelerators. However, accelerators primarily serve as a stepping stone to help startups gain traction, secure early validation, and connect with investors for follow-on funding.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    The pre-seed and seed stages are the ideal capital rounds for companies that want to participate in a university accelerator. These stages align closely with the accelerator’s goal of helping startups refine their products, validate their business models, and prepare for follow-on investment.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    The number of tranches (or stages) in which a company can raise capital through a university accelerator depends on the specific funding structure of the accelerator and the needs of the company. University Accelerators generally provide seed funding in a single tranche but some accelerators may use two or three tranches tied to certain milestones.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    In summary, businesses can use the funds from a university accelerator for various purposes related to product development, team building, marketing, and research. However, there are restrictions on how these funds can be spent, typically to ensure that the money is used to support the startup’s growth and progress.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
   Businesses using a university accelerator must have a moderate to high level of risk tolerance due to the inherent uncertainties of early-stage startups. Founders should be prepared for challenges such as equity dilution, potential failure, and competition for spots in the accelerator. 
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The level of capital cost tolerance a business needs when using a university accelerator is generally moderate. Since university accelerators typically require minimal upfront cash payments, the main capital cost is the equity dilution in exchange for seed funding, resources, and support.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    The upfront costs for a company entering a university accelerator are typically relatively low, as most accelerators are designed to help early-stage startups reduce financial burdens during their initial development stages. The accelerator itself often covers a substantial portion of the program's costs, and in return, companies usually give up a small amount of equity (typically 5-10%) rather than paying high fees upfront. 
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    In general, companies can access initial seed capital within 1 to 2 weeks after being accepted into a university accelerator. The full accelerator program typically lasts 3 to 6 months, with an opportunity to raise additional follow-on funding after demo day, which usually occurs at the end of the program.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)