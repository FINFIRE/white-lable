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


def smallbusinessadministrationcdcsbdc(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Small Business Administration</b></u><br>
    Capital Type: SBDC</center></p>
    
    <p><b><u>Introduction</u></b><br>
    There are more than 1,000 SBDCs operating in all 50 states, the District of Columbia, and many U.S. territories <a href="https://www.occ.gov/publications-and-resources/publications/community-affairs/community-developments-fact-sheets/pub-fact-sheet-ca-sbdc-feb-2016.pdf">(source)</a>. The SBDC provides consulting, training and other services to approximately one million small business owners and aspiring entrepreneurs each year <a href="https://americassbdc.org/about-us/history/">(source)</a>.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br><br>1) Small Business Development Centers provide counseling and training to small businesses including working with SBA to develop and provide informational tools to support business start-ups and existing business expansion.

    <br><br>SBDC Programs deliver professional, high quality, individualized business advising and technical assistance to existing small businesses and pre-venture entrepreneurs. SBDCs provide problem-solving assistance to help small businesses access capital, develop and exchange new technologies, and improve business planning, strategy, operations, financial management, personnel administration, marketing, export assistance, sales and other areas required for small business growth and expansion, management improvement, increased productivity and innovation. (Small Business Development Centers, 2024)

    <br><br>2) The U.S. Small Business Administration (SBA) administers the Small Business Development Centers (SBDC) Program in a cooperative effort with the private sector, the educational community, and federal, state, and local governments to provide management assistance to current and prospective small business owners. 

    <br><br>Each center develops services in cooperation with local SBA district offices to ensure statewide coordination with other available resources. There are now 62 Lead Small Business Development Centers (SBDCs) in every state and territory, with multiple locations that form a network of more than 1000 service locations.

    <br><br>SBDC services include, but are not limited to:
        <br>• Assisting small businesses with financial, marketing, production, organization, engineering and technical problems and feasibility studies
        <br>• Special SBDC programs and economic development activities including international trade assistance, technical assistance, procurement assistance, venture capital formation and rural development

    <br><br>SBDCs also make special efforts to reach minority members of socially and economically disadvantaged groups, veterans, women and the disabled. Assistance is provided to both current or potential small business owners, and to small businesses applying for Small Business Innovation and Research (SBIR) grants from federal agencies. (Office of Small Business Development Centers, 2023)

    <br><br>3) The SBDC provides multiple programs and is usually in business to support businesses by providing resources and access to capital. Most centers work with banks and other lenders to supplement loan applications. Many also provide business owners and operators with the management, marketing and financial skills necessary for their companies to survive and flourish in today’s challenging business environment. (Smith, 2021)
    <br>4) Client confidentiality is mandated by federal law. Information about you or your business will not be shared outside our network without your written permission. 
    <br>Advising services are no cost to you. Funding for SBDC advising and training programs is provided by the U.S. Small Business Administration (SBA), and institutions of higher education, economic development agencies and business and civic organizations.
    <br>When clients first meet with an SBDC advisor they typically establish a scope of work with milestones for what the client wants to achieve. Clients are welcome to return to the SBDC for additional assistance at any time and many do establish long-term relationships that span the lifecycle of their business. (SBDC Services, n.d.)
    </p>
                             
    <u><b><p>References</u></b><br>
    Office of Small Business Development Centers. (2023, November 14). Retrieved from SBA.
    <br><br>SBDC Services. (n.d.). Retrieved from WSBDC: <a href="https://wsbdc.org/sbdc-services/">https://wsbdc.org/sbdc-services/</a>
    <br><br>Small Business Development Centers. (2024, May 31). Retrieved from SBA: <a href="https://www.sba.gov/local-assistance/resource-partners/small-business-development-centers-sbdc">https://www.sba.gov/local-assistance/resource-partners/small-business-development-centers-sbdc</a>
    <br><br>Smith, T. D. (2021). Business Acpital 101. San Francisco: Imaginary Press.
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    There are no legal qualifications, however, the nature of your business and your status as a small business owner will influence your eligibility for some programs or services. Additionally, some specialized programs might have their own eligibility criteria (such as those targeting women-owned or veteran-owned businesses).
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>There are typically no strict document requirements to begin using SBDC services. However, to make the most out of your consultation or counseling session and to receive tailored advice, SBDCs may request certain supporting documents depending on the type of services or guidance you seek. These documents help SBDC advisors understand your business better and provide more effective assistance. The documents can include: 
    <br>• Business Plan 
    <br>• Financial Statements
    <br>• Tax Returns
    <br>• Legal Documents
    <br>• Financial Projections, Business Licenses or Permits
    <br>• Funding or Loan Documentation
    <br>• Marketing Materials
    <br>• Employee Information
    <br>• Personal Financial Information (for certain loan assistance)
    <br>Keep in mind that every SBDC may have slightly different requirements depending on the services you’re requesting or your location. It's a good idea to contact your local SBDC in advance to clarify any document needs specific to your situation.
    </p>
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def smallbusinessadministrationcdcsbdcfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Small Business Administration<br>
    Capital Type: SBDC</center></p>                        
    <p><center><u><b>Frequently Asked Question for SBDC</u></b></center></p>
    <p><u><b>1. What types of capital can I raise through SBA SBDC services?</u></b><br>
    • Answer: Through the SBA SBDC, businesses can seek guidance on raising capital through various SBA-backed loans (e.g., SBA 7(a), SBA 504, microloans), equity financing (e.g., angel investors or venture capital), and government or private grants. The SBDC helps assess your business needs and advises on the best capital options based on your goals and eligibility.</p>
                             
    <p><u><b>2. Are SBA SBDC services free, or do they come with costs?</u></b><br>
    • Answer: Most SBA SBDC services are free or available at a low cost. The SBDC provides consulting and training on business planning, loan preparation, and capital raising without charging for its core services. However, some specific services (e.g., training programs, workshops, third-party consultations) may have associated fees.</p>
                             
    <p><u><b>3. Can the SBA SBDC help me secure capital if my business is just starting out?</u></b><br>
    • Answer: Yes, the SBA SBDC can help startups as well as established businesses. They provide assistance with business plans, financial projections, and loan applications, which are critical for securing funding at the early stages. For startups, they may also help you explore microloans and angel investors.</p>
                             
    <p><u><b>4. How do I know if I’m eligible for an SBA loan or other SBA-backed funding?</u></b><br>
    • Answer: Eligibility for SBA loans typically depends on factors like the size of your business, industry, location, and credit history. The SBDC will review your business plan, financials, and creditworthiness to assess your eligibility and guide you through the application process. They can also help you explore other capital sources if you don’t meet SBA criteria.</p>
                             
    <p><u><b>5. What are the typical costs and fees associated with SBA loans?</u></b><br>
    • Answer: While SBA loans offer favorable terms compared to traditional bank loans, there are still fees involved, including:
    <br>- Loan guarantee fees (typically 0.25% to 3.75% of the loan amount)
    <br>- SBA processing fees
    <br>- Third-party fees for legal, accounting, or appraisals The SBDC will help you understand these costs and determine if an SBA loan is a good financial fit for your business.
    </p>
                             
    <p><u><b>6. How long does it take to secure funding through SBA SBDC services?</u></b><br>
    • Answer: The process typically takes 2 to 3 months for SBA 7(a) and SBA 504 loans, depending on the loan type and completeness of your application. Microloans may take a shorter time frame, around 1 to 2 months. The SBDC helps streamline the process by guiding you through loan preparation and application submission, which can expedite the timeline.</p>
                             
    <p><u><b>7. Can I raise capital from multiple sources (e.g., SBA loan and investors) simultaneously?</u></b><br>
    • Answer:  Yes, businesses can combine capital from different sources, such as an SBA loan and equity financing (angel investors, venture capital) or crowdfunding. The SBDC can help you understand the implications of mixing different funding sources, including any potential impact on ownership, repayment obligations, and financial sustainability.</p>
                             
    <p><u><b>8. What are the key advantages of using SBA SBDC services over traditional lenders or other funding sources?</u></b><br>
    • Answer: The SBDC offers personalized guidance, free or low-cost advisory services, and access to specialized resources to help businesses secure SBA-backed funding. Unlike traditional lenders, the SBDC also assists with crafting business plans, financial projections, and loan packaging, which can increase your chances of approval and help you avoid common pitfalls.</p>
                             
    <p><u><b>9. How can I improve my chances of securing SBA-backed funding?</u></b><br>
    • Answer: The SBDC will work with you to ensure that your business is financially sound and well-prepared for an SBA loan application. This includes ensuring your credit score is competitive, preparing solid financial statements, creating a clear business plan, and addressing any potential concerns that lenders or investors may have. Proper preparation and the right guidance are key to a successful funding application.</p>
                             
    <p><u><b>10. Are there specific industries or types of businesses that are more likely to qualify for SBA funding?</u></b><br>
    • Answer: While SBA loans are available to most businesses, certain industries such as hospitality, manufacturing, and technology may have more opportunities for financing due to their potential for growth and job creation. The SBDC can help you assess your industry’s eligibility and suggest alternative funding sources if SBA loans are not ideal for your business.</p>
                             
    <p><u><b>11. What happens if my SBA loan application is denied?</u></b><br>
    • Answer: If your SBA loan application is denied, the SBDC can help you understand why it was rejected and provide guidance on how to address any weaknesses in your application. You may be able to reapply or explore other capital options, such as microloans, lines of credit, or private investment. The SBDC can also connect you with alternative lenders or funding sources.</p>
                             
    <p><u><b>12. Can the SBA SBDC help me apply for grants?</u></b><br>
    • Answer: Yes, the SBA SBDC can help you find and apply for government or private grants. While grants do not require repayment, the application process is competitive, and the SBDC can guide you through grant writing, eligibility requirements, and submission processes to improve your chances of success.
    </p> 
                             
    <p><u><b>13. How does the SBDC help with raising equity capital (e.g., angel investment, venture capital)?</u></b><br>
    • Answer: The SBDC can provide strategic advice on preparing for equity financing, including creating a pitch deck, business model, and financial projections that attract investors. They can also help connect you with angel investors and venture capitalists through their networks and provide advice on structuring deals to ensure that your business is positioned for growth.</p>

    <p><u><b>14. Can SBA SBDC services help with improving my business’s financial health before seeking capital?</u></b><br>
    • Answer: Yes, the SBDC can assist in improving your business’s financial health before seeking capital by helping you optimize your cash flow, reduce expenses, and increase profitability. They also offer advice on financial forecasting and credit management, which can strengthen your case when applying for capital.</p>
    
     <p><u><b>15. Can the SBA SBDC help me understand my business’s valuation when seeking equity investment?</u></b><br>
    • Answer: Yes, the SBDC can help you assess your business’s valuation through various methods such as market comps, income-based approaches, or asset-based methods. Knowing your business’s valuation is crucial when seeking equity investment, as it helps you negotiate fair terms with investors.</p>
    
    <p><u><b>16. What happens after I secure capital with the help of SBA SBDC services?</u></b><br>
    • Answer: After securing capital, the SBDC can continue to provide advisory services to help you effectively manage your new funds, ensuring you use them for growth, expansion, and meeting financial obligations. The SBDC can also help you track performance metrics, prepare for future funding rounds, and scale your business sustainably.</p>
    
    <p><u><b>17. How do I know which type of capital (loan, equity, grant) is best for my business?</u></b><br>
    • Answer: The SBDC will assess your business model, cash flow, and long-term goals to determine which funding source is the best fit. For example, if you need working capital, an SBA loan might be ideal. If you want to scale quickly and give up some ownership, equity financing might be a better option. The SBDC will help you weigh the pros and cons of each option.</p>             
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def smallbusinessadministrationcdcsbdctwelve(request):
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
    Capital Type: SBA SBDC</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    SBDCs are ideal for businesses at all stages, but the types of support you might need will vary based on your current goals and challenges. If your company is just starting out, SBDCs can be especially helpful in providing foundational support, while established companies can still benefit from expert advice on scaling, expanding, or navigating complex challenges.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    SBDCs provide support to businesses across various entity types. The SBDC can help you navigate the legal, financial, and operational decisions associated with any business structure.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    It’s perfectly acceptable to have raised pre-capital before seeking assistance from the SBDC. In fact, this may provide you with additional opportunities for advanced advice and support as you navigate the complexities of scaling your business and managing your funding. The SBDC’s role is to provide guidance no matter where you are in your business journey, whether you are at the very beginning, already funded, or seeking to expand and grow your operations.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    There are no major restrictions on using SBDC services. The SBDC can offer valuable support, whether you've raised pre-capital through loans, venture capital, personal funds, or other sources. The key is to maintain transparency about your funding structure, including any obligations or restrictions tied to the capital you've raised, so that SBDC advisors can offer the most relevant and effective guidance for your business.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    SBDCs are critical in helping businesses prepare to secure capital through a variety of financing sources. SBDCs offer support in helping businesses apply for SBA-backed loans, microloans, and other types of financing. SBA loans can provide up to $5 million or more, depending on the program but the amount of capital a business can raise depends on the type of funding source, the business’s financial health, and the stage of the business.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    The ideal capital round for a company to use SBA Small Business Development Center (SBDC) services depends on the stage and needs of the business, but typically, the SBDC is most beneficial for businesses at the early stages of their growth or those looking to expand. Seed and Series A rounds are the most ideal as businesses at these stages often need guidance in securing initial funding, developing a solid business plan, and preparing for growth.</p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    You can use one or more tranches when raising funds with the help of SBA SBDC services. Whether it’s through multiple rounds of loans, a combination of equity financing and debt, or blending grants, microloans, and larger SBA loans, the SBDC can support your business at each stage of funding. Their expertise will ensure that your capital raising efforts are well-organized and align with your growth trajectory, helping you navigate each funding round strategically.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    While the SBA SBDC services do not directly provide funds, they can play a crucial role in helping businesses secure funding through SBA loans, traditional loans, grants, equity investments, or crowdfunding. Once funds are secured, the SBDC offers ongoing support to help businesses effectively manage and utilize the funds to grow, scale, or expand. Whether through strategic planning, financial management, or navigating complex funding processes, SBDCs provide valuable expertise to ensure that your business uses capital efficiently to meet its long-term objectives.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    When a business seeks to use SBA Small Business Development Center (SBDC) services, the risk tolerance of the business owner and the company itself plays a significant role in how they approach funding, growth, and strategic decisions. While the SBDC doesn’t directly provide capital, it helps businesses secure financing, grow, and manage their operations, which may involve a certain level of risk.  
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The level of capital cost tolerance required can vary depending on the type of financing the business seeks and its goals. Ultimately, businesses using SBA SBDC services should evaluate their financial capacity, long-term goals, and willingness to bear the costs associated with different forms of capital.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    The SBA SBDC services themselves are typically free of charge or available at minimal costs. The SBDC will be able to advise on average upfront costs the business will encounter using different capital markets. 
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    The speed at which a company can secure capital through SBA SBDC services depends on several factors, including the type of financing sought, the preparation level of the business, and the efficiency of the loan application process. The SBA SBDC helps businesses navigate processes and reduce delays by assisting with application preparation and connecting businesses with the right funding opportunities.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)