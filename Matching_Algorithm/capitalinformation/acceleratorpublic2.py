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


def acceleratorpublic(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Accelerator</b></u><br>
    Capital Type: Public</center></p>
    <p><b><u>Introduction</u></b><br>Research published in 2024 found that startups that went through an accelerator raised 50% to 170% more from investors than did similar startups that applied but were not accepted into the same accelerators. Similarly, a 2014 study found that metropolitan statistical areas (MSAs) that gain an accelerator experienced a 104% increase in venture capital deals across the MSA.<a href="https://crsreports.congress.gov/product/pdf/IF/IF12794/2">(source)</a> According to research, the global startup accelerator market was valued at $1.15 billion in 2020 and is projected to reach $2.55 billion by 2027.<a href="https://www.linkedin.com/pulse/startup-accelerator-market-size-2024-analysis-dguye">(source)</a></p>
    
    <p>172 U.S.-based accelerators were in existence during the 2005–2015 period. Collectively, they invested in more than 5,000 U.S. startups. During this period, these companies have raised a total of $19.5 billion in funding, a number that will surely increase as accelerator programs continue to turn out companies and recent graduates work their way to maturity.<br>Accelerator graduates that went on to raise additional venture capital investment had a median valuation of $15.6 million during this period, and an average valuation of $90 million. Some very well-known companies belong to this group, including “unicorns” AirBnB, Dropbox, and Stripe, among others.<a href="https://hbr.org/2016/03/what-startup-accelerators-really-do">(source)</a></p>
   
    <p><b><u>Definition of Capital Type</b></u><br>
    1) An accelerator is an organization that typically helps startup and early-stage companies mature and grow their businesses. Accelerators generally provide a structured training program over several months, extensive mentoring for the company founders, some limited capital investment, and access to additional investors, and other services. One of the most important values provided by accelerators is access to mentor networks that can facilitate early market validation, allowing companies to prove they have a product somebody would be willing to buy. Entrepreneurs additionally derive great value from the innovation environment, interacting with a group of people who share similar interests, and experiences in starting new businesses. (Accelerator FAQs, 2024)</p>
                             
    <p>2) A business accelerator is a program that gives developing companies access to mentorship, investors, and other support that can help them become stable and self-sufficient. Companies that use business accelerators are generally startups that have moved beyond the earliest stages of getting established. They have entered into ‘adolescence’, meaning that they can stand on their own two feet but need guidance and peer support to gain strength. An accelerator program can last anywhere for two to six months. The goal is for the company to emerge ready to stand on their own, with strong positioning to claim a share of their target markets. (Smith, 2021)</p>
                             
    <p>3) The accelerator experience is a process of intense, rapid, and immersive education aimed at accelerating the life cycle of young innovative companies, compressing years’ worth of learning-by-doing into just a few months.</p>
                             
    <p>Susan Cohen of the University of Richmond and Yael Hochberg of Rice University highlight the four distinct factors that make accelerators unique: they are fixed-term, cohort-based, and mentorship-driven, and they culminate in a graduation or “demo day.” None of the other previously mentioned early-stage institutions — incubators, angel investors, or seed-stage venture capitalists — have these collective elements. Accelerators may share with these others the goal of cultivating early-stage startups, but it is clear that they are different, with distinctly different business models and incentive structures. (Hathaway, 2016)</p>
                             
    <p>4) To pick the right accelerator for your business, you must: 
    <br>&emsp;• Define what you want to get out of the program.
    <br>&emsp;• Research programs that fit your business model.
    <br>&emsp;• Consider the location, cost, and time commitment required by each accelerator.
    <br>Accelerators can provide startups with much-needed resources like access to capital, mentorship, and networking opportunities. But don’t forget that every accelerator is different — it’s up to you to do your research and find the right fit for your business. (What Is a Business Accelerator? Everything You Need To Know, 2023)</p>
                             
    <u><b><p>References</u></b><br>
    Accelerator FAQs. (2024, September 19). Retrieved from Department of Homeland Security : <a href="https://www.dhs.gov/archive/science-and-technology/accelerator-faqs">https://www.dhs.gov/archive/science-and-technology/accelerator-faqs</a></p>
                             
    <p>Hathaway, I. (2016, March 1). What Startup Accelerators Really Do. Retrieved from Harvard Buisiness Review : <a href="https://hbr.org/2016/03/what-startup-accelerators-really-do">https://hbr.org/2016/03/what-startup-accelerators-really-do</a></p>
                             
    <p>Smith, T. D. (2021). Business Capital 101. Imaginary Press.</p>

    <p>What Is a Business Accelerator? Everything You Need To Know. (2023, January 16). Retrieved from Hub Spot: <a href="https://www.hubspot.com/startups/resources/what-is-an-accelerator">https://www.hubspot.com/startups/resources/what-is-an-accelerator</a></p>                                                  
                                                          
    <p><u><b>Legal Qualification Requirements</u></b>
    <br>• Business Plan
    <br>• Financial Statements
    <br>• Financial Projections
    <br>• Corporate Documents
    <br>• Ownership and Equity Structure
    <br>• Intellectual Property (IP) Documentation
    <br>• Board and Governance Documentation
    <br>• Investment Offering Documents
    <br>• Investor Agreements
    <br>• AML and KYC Compliance Forms
    <br>• Investor Protection and Disclosure Statements
    <br>• Exit Strategy and Liquidity Plan
    <br>• Use of Funds Breakdown
    <br>• Tax Compliance Documents</p>
                                 
    <p><b><u>Supporting Document List</u></b>
    <br>• Business Plan
    <br>• Financial Statements
    <br>• Financial Projections
    <br>• Corporate Documents
    <br>• Ownership and Equity Structure
    <br>• Intellectual Property (IP) Documentation
    <br>• Board and Governance Documentation
    <br>• Investment Offering Documents
    <br>• Investor Agreements
    <br>• AML and KYC Compliance Forms
    <br>• Investor Protection and Disclosure Statements
    <br>• Exit Strategy and Liquidity Plan
    <br>• Use of Funds Breakdown
    <br>• Tax Compliance Documents
    <br>• ESG Compliance Statements (if applicable)
    <br>• Legal Certifications and Compliance Statements
    <br>• Prior Funding Documents</p>                                                                       
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def acceleratorpublicfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Accelerator<br>
    Capital Type: Public</center></p>                        
    <p><center><u><b>Frequently Asked Question for Commercial Bank Loans</u></b></center></p>
                             
    <p><u><b>1. What is a public accelerator, and how does it differ from other funding options?</u></b><br>
    •Answer: A public accelerator is a program typically supported by government or non-profit organizations that provides startups with capital, mentorship, resources, and networking opportunities to help them scale quickly. It differs from traditional funding sources like venture capital because it usually offers equity-based funding in exchange for mentorship and program access rather than solely focusing on financial investment.</p>
                             
    <p><u><b>2. What types of businesses are best suited for a public accelerator?</u></b><br>
    • Answer: Public accelerators typically target early-stage startups, often in the pre-seed or seed stage, that are still refining their product, market fit, and business model. Companies that are technology-driven, innovative, or socially impactful often align well with public accelerators.</p>
                             
    <p><u><b>3. How much funding can I expect to receive from a public accelerator?</u></b><br>
    • Answer: The amount of funding varies, but most public accelerators offer between $20,000 to $150,000 in exchange for a 5-10% equity stake. This funding is often seed capital that helps the business during the early development phases, such as product refinement, team building, or initial market testing.</p>                             
                             
    <p><u><b>4. How quickly can I access the capital after being selected?</u></b><br>
    • Answer: Once selected, businesses typically receive initial funding within 1 to 4 weeks of joining the accelerator program. The capital is often provided in the form of a convertible note, SAFE (Simple Agreement for Future Equity), or an equity investment, and may be distributed early in the program to help the company meet initial milestones.</p>
                             
    <p><u><b>5. What are the costs of participating in a public accelerator?</u></b><br>
    • Answer: Upfront costs are generally low for public accelerators, with application fees ranging from $0 to $200 (if applicable). The biggest cost is the equity dilution (usually 5-10%) in exchange for funding, mentorship, and resources. Some accelerators also provide financial support for travel and accommodation, while others may require the company to cover those expenses.</p>
                             
    <p><u><b>6. Do I have to give up equity in exchange for the accelerator's funding?</u></b><br>
    • Answer: Yes, most public accelerators take equity in exchange for the capital and services they provide, typically between 5-10%. This means you will be giving up ownership and control of your company in exchange for resources that could help you scale quickly. The equity trade-off should be weighed against the potential long-term benefits of the program.</p>
                             
    <p><u><b>7. Can a company still raise capital from other sources while in a public accelerator?</u></b><br>
    • Answer: Yes, startups in public accelerators are often encouraged to raise additional capital during or after the program, particularly at demo days or investor pitch events organized by the accelerator. However, depending on the terms of the accelerator, there might be some restrictions on raising outside capital during the program or preference terms with investors the accelerator brings in.</p>
                             
    <p><u><b>8. What are the key benefits of joining a public accelerator over traditional VC funding?</u></b><br>
    • Answer: Public accelerators offer a unique combination of equity-based funding, mentorship, networking, and resources. Unlike traditional venture capital (VC), public accelerators often focus on early-stage support, providing resources for businesses still in product development or customer acquisition. Additionally, they may offer government-backed support, lower equity dilution, and lower upfront costs, which can be advantageous for startups.</p>
                             
    <p><u><b>9. What resources and support can I expect from a public accelerator?</u></b><br>
    • Answer: Public accelerators typically provide a wide range of mentorship, workshops, networking events, and office space. They often have partner organizations (e.g., law firms, accountants, marketing agencies) that offer discounted or free services. Some accelerators also provide access to potential investors, partnerships, or public sector funding to further support growth.</p>
                             
    <p><u><b>10. What happens after the accelerator program ends?</u></b><br>
    • Answer: After completing the program, you will have the opportunity to participate in a demo day or investor pitch events where you can present your business to potential investors. Public accelerators also often provide follow-up support, such as connecting you with additional funding opportunities, providing introductions to key industry players, or helping you secure seed or Series A funding.</p>
                             
    <p><u><b>11. Are there any risks associated with using a public accelerator?</u></b><br>
    • Answer: While public accelerators offer many benefits, there are also risks. These include equity dilution (5-10%), the opportunity cost of time spent in the program, and the possibility that the accelerator’s network may not be the best fit for your specific industry. Additionally, while accelerators can help with early-stage growth, they do not guarantee long-term success or securing follow-on funding.</p>
                             
    <p><u><b>12. How does a public accelerator compare to other forms of funding, such as angel investors or venture capital?</u></b><br>
    • Answer: Public accelerators offer a more hands-on approach to supporting startups compared to angel investors or venture capital. While VCs and angel investors typically offer capital in exchange for equity, accelerators provide mentorship, guidance, resources, and access to networks that may be more beneficial at the early stage. Accelerators also tend to have a lower cost of entry (equity-wise) compared to traditional investors, who may demand higher stakes in exchange for capital.</p>
                             
    <p><u><b>13. Can I participate in a public accelerator if I have already raised capital from other sources?</u></b><br>
    • Answer:   Yes, many accelerators accept companies that have already raised some initial capital, as long as they are still in the early stages. However, some accelerators may have specific eligibility criteria regarding the amount of funding raised, or they may prefer startups with limited external investment to avoid conflicts of interest.</p> 
                             
    <p><u><b>14. What type of companies typically get accepted into public accelerators?</u></b><br>
    • Answer:  Public accelerators tend to focus on companies that are technology-driven, innovative, and have the potential for significant scalability. Companies in fields like tech, cleantech, healthcare, fintech, and social enterprises are often well-suited for public accelerators. However, each accelerator program may have its own focus area or industry preference.</p>
                             
    <p><u><b>15. How can I increase my chances of being accepted into a public accelerator?</u></b><br>
    • Answer: To increase your chances of being accepted, you should have a clear business plan, demonstrate a strong founding team, and show traction (e.g., customer validation, early sales, or a working prototype). Being able to articulate a scalable solution to a significant problem and how the accelerator’s resources can help you achieve your goals is key. Researching the specific requirements of the accelerator and tailoring your application to their focus areas can also increase your chances.</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def acceleratorpublictwelve(request):
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
    Public Accelerator</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    The ideal stage for a company to join a public accelerator is pre-revenue to early revenue; primarily when they are refining their product, testing market fit, and preparing for growth. Public accelerators typically focus on providing these startups with the guidance, mentorship, and resources they need to scale and secure funding.</p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    The C-Corp is typically the most ideal entity type for a business looking to use a public accelerator, especially if the company plans to seek venture capital or significant investment. It aligns well with the goals of growth, scalability, and attracting investors. LLCs and S-Corps can also work, especially for businesses not seeking large-scale external funding but still looking for mentorship and guidance. Sole proprietorships and partnerships can benefit from accelerators but are often less likely to be chosen by accelerators focused on high-growth potential or investment.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    The restrictions on pre-existing capital before joining a public accelerator depend largely on the accelerator's focus and the stage of startups it supports. Accelerators generally prefer early-stage companies that have raised minimal funding, as they are more likely to need the kind of support accelerators provide. Businesses that have raised significant funding (e.g., Series A or beyond) may be considered too far along to benefit from these programs.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    While many accelerators are open to startups at various stages, how capital has been raised (particularly in terms of venture capital or equity-based investments) could interfere with participation in some programs. Accelerators may have specific funding-stage preferences, restrictions on previous funding sources, or rules regarding equity dilution that influence whether a company is eligible. 
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    While public accelerators themselves usually provide early-stage funding (typically around $20,000 to $150,000), the real opportunity comes in the form of follow-on investments, prizes, and networking that help companies raise larger rounds of funding after graduating from the program.
    </p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Pre-seed companies are the best fit for public accelerators because these programs are specifically designed to help startups with limited resources, unproven products, and little customer traction. Seed rounds are still common for accelerator participation, especially for companies that are refining their product and scaling their customer base.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    For most startups using a public accelerator, a single tranche raise is typically sufficient at the pre-seed or early seed stage. This initial investment helps get the company off the ground, refine the business model, and prepare for larger follow-on rounds.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    While accelerator funds are typically flexible, some restrictions may apply to ensure the funds are used appropriately for business growth. The funds are generally meant for product development, marketing and customer acquisition, team building and operational expenses. Restrictions generally focus on preventing misuse of funds for personal expenses, unrelated ventures, or debt repayment. Most accelerators will provide guidelines on fund usage, but the funds are typically intended to support the company’s growth toward its next fundraising round or scaling goals.</p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    A business entering a public accelerator needs to have a high risk tolerance due to the inherent uncertainties at the early stage. They face the possibility of product-market fit challenges, equity dilution, and the uncertainty of future fundraising rounds. The program requires a significant time commitment and may offer limited resources, with competition from other startups. There are also potential regulatory risks and legal issues, especially in specific industries. 
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    Businesses using a public accelerator should have a moderate to high level of capital cost tolerance and be prepared for the cost of equity dilution, the need for future funding, and the potential financial risks associated with the program. The ideal business should have the flexibility and willingness to invest resources to accelerate growth, while understanding the trade-offs involved in the process.
    </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    Public accelerators are designed to minimize upfront costs for startups, especially those that are early-stage or without significant funding. However, companies should be prepared to cover legal, travel, and operational costs during the program that can range from $2,000 to $9,000. Equity dilution remains the most significant long-term consideration.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    Companies can expect to receive initial capital quickly, often within a few weeks to a month after being selected. The selection process may take 2-3 months depending on the program. Subsequent funding from the accelerator or follow-up investors will typically take longer, as it depends on progress and milestones met during the accelerator program.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)