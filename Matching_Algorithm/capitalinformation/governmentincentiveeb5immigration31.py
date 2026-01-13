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


def governmentincentiveeb5immigration(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Government Incentives</b></u><br>
    Capital Type: EB5 Immigration</center></p>
    
    <p><b><u>Introduction</u></b><br>
    The EB-5 Immigrant Investor Program is ideal for companies seeking to raise capital while offering foreign investors a pathway to U.S. residency. This program allows foreign nationals to invest a minimum of $800,000 in a targeted employment area (TEA) or $1 million in other areas, in exchange for job creation and economic development. {name} fits this profile, as it is positioned to benefit from foreign investment through the EB-5 program. Since its inception in 1990, the EB-5 program has raised billions of dollars, with over $1.5 billion raised in 2023 alone. The program has proven to be a viable capital-raising tool, with the total amount of EB-5 investment projects reaching significant sums each year. For example, in 2023, over 1,500 investors participated in EB-5-funded projects, creating thousands of jobs and driving U.S. economic growth. By utilizing the EB-5 program, {name} can attract international capital, fueling expansion while providing foreign investors with a unique opportunity to secure U.S. residency. However, it is important to note that the program carries risks, including the potential loss of capital, as investments are tied to the success of the funded business, and there is no guarantee of returns or job creation.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br>1. The EB-5 Immigrant Investor Program is a U.S. government initiative that allows foreign nationals to obtain permanent residency in the United States by making a qualifying investment in a U.S. business. The program requires a minimum investment of $1 million (or $800,000 in a Targeted Employment Area, or TEA) into a new commercial enterprise that will create or preserve at least 10 full-time jobs for U.S. workers. This pathway provides foreign investors and their immediate families (spouse and children under 21) an opportunity to live and work in the U.S., while contributing to the U.S. economy through capital infusion and job creation.
<br>
    <br>Since its inception in 1990, the EB-5 program has attracted billions of dollars in foreign investment, supporting thousands of U.S. businesses and creating numerous jobs. In 2023 alone, the program raised over $1.5 billion through the participation of over 1,500 investors. The program is managed by U.S. Citizenship and Immigration Services (USCIS), which adjudicates investor petitions and ensures compliance with the requirements. However, it is important to note that the program carries risks, including the potential loss of capital, as the investment is subject to the success of the business. Investors must also meet specific criteria for job creation and comply with ongoing program regulations. (USCIS, 2023)
    <br><br>2. There are two primary investment thresholds for the EB-5 program:
    <br>• $1 million for investments in non-Targeted Employment Areas (TEAs), which typically include regions with lower unemployment rates.
<br>
    <br>• $800,000 for investments in Targeted Employment Areas (TEAs), which are designated areas with high unemployment or rural areas. TEAs are intended to encourage investment in economically disadvantaged regions to stimulate growth and job creation. The investor's capital must be at risk, and the business must be structured to create at least 10 full-time, permanent jobs for U.S. workers within two years of the investor's admission to the U.S. (USCIS, 2023)
<br>
    <br>3. For a company to utilize the EB-5 Immigrant Investor Program, it can be sponsored by a Regional Center, which is a U.S. government-approved entity designated to oversee EB-5 investment projects. A Regional Center is typically responsible for managing the pooling of funds from multiple investors, often focusing on large-scale projects in specific geographic areas. By working with a Regional Center, the company can benefit from the ability to count indirect and induced jobs toward the EB-5 job creation requirement, making it easier to meet the necessary employment thresholds. This is especially helpful for businesses where direct job creation may be challenging. Regional Centers also handle much of the regulatory and reporting compliance, streamlining the process for the company and its investors. While it is not a requirement for all EB-5 investments, being sponsored by a Regional Center can enhance the company’s ability to attract EB-5 investors and ensure the program's success.
<br>
    <br>4. The EB-5 process typically takes several years from start to finish. After making the investment, the foreign investor files a petition (Form I-526) to demonstrate that the investment meets program requirements. Upon approval, the investor and their family can apply for conditional permanent residency. After two years of conditional residency, the investor must file a Form I-829 petition to remove conditions and obtain full, permanent residency status. The entire process, from investment to permanent residency, can take 3 to 5 years depending on various factors, such as USCIS processing times and the specific investment project’s performance. Delays in processing or failure to meet job creation or other program requirements could result in denials or delays. (USCIS, 2023)
<br>
    <br>5. The EB-5 Immigrant Investor Program presents several risks for companies. Key risks include meeting the job creation requirement (at least 10 full-time jobs per investor), which if unmet, could result in investor denial of residency and reputational harm. Companies must also comply with complex regulatory requirements, and failure to do so could lead to penalties or disqualification. Additionally, the program’s investment risk involves the potential loss of capital if the business fails, which could result in legal challenges. (USCIS, 2023)
<br>
    <br>The EB-5 process is lengthy, often taking years, creating uncertainty around funding. Companies must also avoid fraud or misrepresentation, as this could lead to legal and reputational damage. The reliance on foreign investment adds further risk, as changes in international relations or economic conditions could impact capital flow. Effective legal oversight, transparency, and planning are essential to mitigate these risks. (DHS, n.d.)
    </p>
                             
    <u><b><p>References</u></b><br>
    <br>EB-5 Immigrant Investor Program | USCIS. (2023, March 1). USCIS. <a href="https://www.uscis.gov/working-in-the-united-states/permanent-workers/eb-5-immigrant-investor-program">https://www.uscis.gov/working-in-the-united-states/permanent-workers/eb-5-immigrant-investor-program</a>
    <br>
    <br>Immigrant investor visas. (n.d.). <a href="https://travel.state.gov/content/travel/en/us-visas/immigrate/immigrant-investor-visas.html">https://travel.state.gov/content/travel/en/us-visas/immigrate/immigrant-investor-visas.html</a>
    <br>
    <br>Invest in the USA. (2024, April 3). About EB-5 - EB-5 Immigration Services - Invest in the USA. <a href="https://iiusa.org/education/about-eb-5/">https://iiusa.org/education/about-eb-5/</a>
    <br>
    <br>Damsgaard, M. (2025, February 28). EB5 Visa Program Guide: key benefits and application process. Global Residence Index. <a href="https://globalresidenceindex.com/usa-eb5-investor/#:~:text=Navigating%20Immigration%20Law,petition%20for%20lawful%20permanent%20residence">https://globalresidenceindex.com/usa-eb5-investor/#:~:text=Navigating%20Immigration%20Law,petition%20for%20lawful%20permanent%20residence.</a>
    <br>
    <br>Moodie, A. (2025, February). The EB-5 investor Visa, explained. Boundless. Retrieved April 2, 2025, from <a href="https://www.boundless.com/immigration-resources/eb-5-investor-visa-explained/">https://www.boundless.com/immigration-resources/eb-5-investor-visa-explained/</a>
    <br>
    <br>The CIS Ombudsman’s Webinar Series: Engagement with USCIS on the EB-5 Immigrant Investor Program | Homeland Security. (n.d.). U.S. Department of Homeland Security. <a href="https://www.dhs.gov/publication/cis-ombudsmans-webinar-series-engagement-uscis-eb-5-immigrant-investor-program">https://www.dhs.gov/publication/cis-ombudsmans-webinar-series-engagement-uscis-eb-5-immigrant-investor-program</a>
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>• Eligible Business Type: The company must be a for-profit business engaged in commercial activity, either a new or troubled enterprise.
    <br>• Job Creation: The company must create at least 10 full-time U.S. jobs for each investor within two years.
    <br>• Investment Requirements: The business must receive an investment of $1 million (or $800,000 in a TEA) from the investor.
    <br>• Capital At Risk: The invested funds must be at risk and used to foster economic activity and job creation.
    <br>• Regional Center (Optional): The company can partner with a Regional Center to manage pooled investments, allowing indirect job creation to count.
    <br>• Business Structure: The company must be a corporation, limited partnership, or similar entity.
    <br>• Proof of Viability: The company must demonstrate a credible business plan and the capacity to create jobs and economic growth.
    <br>• Ongoing Compliance: The company must comply with EB-5 regulations and provide periodic reports on fund usage and job creation.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Form I-526: The primary petition form for EB-5 applicants.
    <br>• Proof of Investment: Documents showing the investor’s capital investment, such as bank statements, wire transfers, or purchase agreements. Also, evidence that the funds are at risk (e.g., business plan, financial statements).
    <br>• Source of Funds: Documentation proving the legal origin of the investment funds, such as bank statements, tax returns, or sale agreements.
    <br>• Business Plan: A detailed plan outlining how the business will create at least 10 full-time U.S. jobs, including financial projections and job creation strategies.
    <br>• Regional Center Documents (if applicable): If using a Regional Center, provide the center’s designation letter and project approval documents from USCIS.
    <br>• Investor Identification: Passport copies and birth certificates for the investor and any family members included in the petition.
    <br>• Proof of Lawful Entry: For applicants already in the U.S., evidence of lawful entry, such as an I-94 or visa stamp.
    <br>• Other Forms: Additional forms like Form I-485 (if adjusting status in the U.S.) or Form DS-260 (for immigrant visas).
    </p>
        """)
    
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
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,name=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def governmentincentiveeb5immigrationfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Government Incentives <br>
    Capital Type: EB5 Immigration</center></p>                        
    <p><center><u><b>Frequently Asked Question for EB5 Immigration</u></b></center></p>
    <p><u><b>1. What is the EB-5 Immigrant Investor Program?</u></b><br>
    • Answer: The EB-5 program is a U.S. visa program that allows foreign nationals to obtain permanent residency (a Green Card) by investing in a U.S. business that creates jobs for U.S. workers. The minimum investment is $1 million (or $800,000 in a Targeted Employment Area, or TEA).
    </p>
                             
    <p><u><b>2. How much money do I need to invest to qualify for the EB-5 program?</u></b><br>
    • Answer: You must invest $1 million in a U.S. business, or $800,000 if the investment is made in a Targeted Employment Area (TEA), which is a rural area or one with high unemployment.
    </p>
                             
    <p><u><b>3. What are the requirements for job creation?</u></b><br>
    • Answer: The business must create at least 10 full-time jobs for U.S. workers within two years of the investor's admission to the U.S. Jobs can be direct (from the business itself) or indirect (through a Regional Center investment).
    </p>
                             
    <p><u><b>4. Can I invest through a Regional Center?</u></b><br>
    • Answer: Yes, you can invest through a USCIS-approved Regional Center, which manages pooled investments in large-scale projects. Regional Centers allow for indirect job creation, making it easier to meet the job creation requirement.</p>
                             
    <p><u><b>5. How long does the EB-5 process take?</u></b><br>
    • Answer: The EB-5 process can take several years. Typically, it takes around 18-24 months for the initial EB-5 petition (Form I-526) to be processed. After approval, it may take additional time to obtain permanent residency.
    </p>
                             
    <p><u><b>6. What are the risks of the EB-5 program?</u></b><br>
    • Answer:     
    <br>• Investment loss: There's no guarantee that the investment will succeed, and you could lose your capital.
    <br>• Job creation failure: If the business does not create the required 10 jobs, the investor may lose eligibility for a Green Card.
    <br>• Regulatory changes: Changes in immigration or securities laws can impact the process and outcome.
    </p>
                             
    <p><u><b>7. Can my family join me through the EB-5 program?</u></b><br>
    • Answer: Yes, the EB-5 program allows you to include your spouse and unmarried children under the age of 21 in your petition for permanent residency.</p>
                             
    <p><u><b>8. What is the difference between direct investment and Regional Center investment?</u></b><br>
    • Answer: 
    <br>- Direct Investment: You invest directly in a business and are more actively involved in its management. You are responsible for creating 10 direct jobs.
    <br>- Regional Center Investment: You invest through a USCIS-approved Regional Center, which pools investments for larger projects. Indirect job creation can count toward the job requirement.
    </p>
                             
    <p><u><b>9. What documentation is required to apply for the EB-5 visa?</u></b><br>
    • Answer:     
    <br>- Form I-526 (Immigrant Petition)
    <br>- Proof of investment and source of funds
    <br>- Business plan demonstrating job creation
    <br>- Passport copies and personal identification documents
    <br>- Evidence of lawful entry (if applying from within the U.S.)</p>
                             
    <p><u><b>10. What happens if my EB-5 petition is denied?</u></b><br>
    • Answer: If your I-526 petition is denied, the investor and their family are not eligible for a Green Card. The investment may be refunded, but it depends on the terms of the investment agreement.</p>                                                   
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def governmentincentiveeb5immigrationtwelve(request):
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
    Capital Type: Accounts Recievable Loans</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    {n} is in the Startup stage and seeking to expand its operations. The EB-5 Immigrant Investor Program presents an opportunity to raise significant capital from foreign investors, offering up to $1 million per investor in exchange for creating at least 10 full-time jobs per investor. This capital infusion will help {n} accelerate its growth, expand operations, and enhance its market presence while securing U.S. residency for the investors.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Utilizing the EB-5 program for a C Corporation is an ideal option for {n}. This entity type allows for clear ownership structures and is eligible for the EB-5 program, which mandates the creation of jobs and meets the legal requirements of the U.S. Citizenship and Immigration Services (USCIS). C Corporations are also well-suited for handling large-scale investments from foreign nationals.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    {n} has already raised initial capital, which positions the company to use the EB-5 program as a strategic next step to raise further funds. The pre-existing capital can be leveraged for initial growth, and the EB-5 investment will provide a strong foundation for more substantial funding to scale the company significantly. With each investor contributing $1 million (or $800,000 in TEA areas), the company can expand its operations while meeting the job creation criteria.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    Having already raised initial funding through traditional methods, {n} is well-positioned to move forward with the EB-5 program. This next step allows the company to access a broader pool of investors, particularly international investors seeking U.S. residency through their investments, which significantly increases the capital-raising potential beyond previous funding rounds.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    With the EB-5 program allowing companies to raise up to $1 million per investor (or $800,000 in TEA), {n} is in a favorable position to raise substantial capital to meet its goals. Depending on the total number of investors, {n} could raise significant amounts, helping to fund its expansion while creating jobs and securing long-term growth.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Since {n} is in the early stages of scaling its operations, the EB-5 program provides a viable path to attract international investors. This capital-raising method allows the company to pool resources from multiple investors while ensuring compliance with USCIS guidelines for job creation and economic development. The flexible terms of the EB-5 program make it an ideal option for fast-growing companies like {n}.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    The EB-5 program allows the structuring of funding in multiple rounds (or tranches), which gives {n} the flexibility to raise capital in phases. The company can target specific milestones and valuation triggers to raise the necessary funds in manageable increments, ensuring steady progress and maintaining investor confidence as it expands its operations.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Funds raised through the EB-5 program can be used for a variety of business needs, providing flexibility for {n}. The capital may be used for expansion, hiring, product development, marketing efforts, and working capital. The company must clearly outline these uses in the offering documents to ensure full compliance with the EB-5 program and transparency with investors.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    The main risks of using the EB-5 program for {n} include the potential challenges of meeting the job creation requirement, as failure to create 10 full-time jobs per investor could result in the denial of permanent residency for investors. Additionally, changes in immigration policy or business performance could affect the success of the program. Proper planning and strong legal oversight are critical to mitigate these risks.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The EB-5 program requires a substantial investment of at least $800,000 per investor, which {n} can use to fuel its expansion. The program’s requirements for job creation and ongoing reporting mean that there will be costs associated with regulatory compliance, legal services, and project oversight. However, with proper planning, these costs can be managed to maximize the benefits of raising foreign investment capital.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    The initial costs for an EB-5 offering typically range from $50,000 to $100,000 or more, covering the expenses for legal counsel, USCIS filings, business planning, and investor marketing. {n} should plan for these expenses, particularly when structuring the offering and ensuring the necessary legal and operational compliance. Careful budgeting for these costs is essential to avoid unforeseen expenses.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    The EB-5 process can take longer than traditional funding methods, with an estimated timeline of 12 to 24 months from the initial petition (I-526) submission to the approval of permanent residency. However, once the petition is approved and the capital is raised, {n} can start utilizing the funds for expansion and growth. The timeline for raising the necessary capital through the EB-5 program is longer compared to traditional fundraising, but it offers significant advantages for businesses seeking substantial foreign investment.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)