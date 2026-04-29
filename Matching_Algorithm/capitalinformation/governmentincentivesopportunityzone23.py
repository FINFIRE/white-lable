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


def governmentincentivesopportunityzone(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""<p><center><b><u>Definition of Capital Market: Government Incentives</b></u><br>

    Capital Type: Opportunity Zone Tax Credit Fund </center></p>

    <p><b><u>Introduction</u></b><br>

Opportunity Zone (OZ) Tax Credit Funds are ideal for companies seeking equity investment from taxpayers with realized capital gains, including support for real estate development, infrastructure, and business expansion in distressed communities. They are designed so that government-legislated tax incentives can help privately held startups and enterprises grow in low-income census tracts, fostering economic revitalization and job creation. {n} fits that definition. Opportunity Zone funds have been a rapidly growing tool for community development since their creation in 2017. For example, by the end of 2019, Qualified Opportunity Funds (QOFs) had already raised approximately $75 billion in private capital to be deployed in over 8,700 designated zones across the United States. The program is widely used for multi-family housing, renewable energy projects, and scaling operating businesses within these zones. On average, OZ-backed projects gain access to substantial equity capital from high-net-worth individuals and family offices, with the added benefit of potentially eliminating 100% of capital gains taxes on the fund's appreciation if held for 10 years. While Opportunity Zones offer powerful tax advantages, the high risk associated with investing in distressed areas, complex IRS compliance requirements, and the necessity of a long-term (10-year) holding period can limit flexibility for some investors and companies.    </p>

 

    <p><b><u>Definition of Capital Type</b></u><br>

    <br>1.	Opportunity Zone Tax Credit Funds, legally known as Qualified Opportunity Funds (QOFs), are private investment vehicles (corporations or partnerships) organized for the specific purpose of investing in Qualified Opportunity Zone property. Created by the Tax Cuts and Jobs Act of 2017, these funds allow investors to reinvest capital gains from any asset sale—such as stocks, real estate, or a private business—into designated low-income communities. The primary mechanism is tax relief: deferring current capital gains taxes and providing tax-free growth on the new investment. (IRS.gov, 2025)

<br>



    <br>2.	The best type of companies to raise money via Opportunity Zone funds are those located within, or willing to move to, a designated Opportunity Zone. These companies typically include real estate developers, manufacturing plants, and tech startups that meet the "Qualified Opportunity Zone Business" (QOZB) criteria. To qualify, a business must derive at least 50% of its gross income from active conduct within the zone and ensure "substantially all" of its tangible property is located there. These companies benefit most when they have a long-term growth horizon (10+ years) to maximize the tax-free exit for their investors. (Investopedia, 2024)

<br>


    <br>3.	Opportunity Zones emerged from a bipartisan initiative spearheaded by Senators Cory Booker and Tim Scott, based on research into geographical economic inequality following the Great Recession. Modeled after previous "Enterprise Zones" but using a broader, market-driven approach, the program was officially launched in 2018. Over 8,760 census tracts were nominated by state governors and certified by the U.S. Treasury, representing roughly 12% of all U.S. census tracts. Since inception, the program has evolved from a real-estate-heavy model to one that increasingly supports "operating businesses" in diverse sectors like climate tech and healthcare. (Economic Innovation Group, 2023)

<br>

    <br>4.	While OZ funds offer massive tax upside, companies face significant regulatory risks. A QOF must hold at least 90% of its assets in qualified property; failure to meet this "90% Asset Test" results in monthly penalties. Additionally, for real estate projects, the property must be "substantially improved," meaning the fund must invest an amount into improvements equal to or greater than the original cost of the building within 30 months. Reliance on these funds also introduces a "lock-in" effect, as the greatest tax benefits are only realized after a decade of continuous investment. (Local Initiatives Support Corporation, 2025)

<br>

    <br>5.	To raise capital via an Opportunity Zone fund, a company must demonstrate its status as a Qualified Opportunity Zone Business (QOZB). This requires showing that at least 70% of the tangible property owned or leased by the business is "Qualified Opportunity Zone Business Property." Companies must present a clear compliance plan to investors, proving they can meet the income and asset tests required by the IRS. Successful fundraising often involves working with specialized OZ fund managers or creating a "captive" fund for a single specific project. (Saul Ewing LLP, 2024)
    </p>

                            

    <p><u><b>References</u></b><br>


     <br>Investopedia. (2024, November 15). Opportunity Zone: Meaning, Advantages, Criticism.  <a href="https://www.investopedia.com/opportunity-zone-5207933">https://www.investopedia.com/opportunity-zone-5207933</a>

<br>

   <br>Economic Innovation Group (EIG). (2023, June 14). About Opportunity Zones.  <a href="https://eig.org/opportunity-zones/about-ozs/">https://eig.org/opportunity-zones/about-ozs/</a>

<br>

   <br>Local Initiatives Support Corporation (LISC). (2025). Opportunity Zones 101.  <a href="https://www.lisc.org/our-resources/resource/opportunity-zones-101/">https://www.lisc.org/our-resources/resource/opportunity-zones-101/</a>

<br>

   <br>Saul Ewing LLP. (2024). Opportunity Zones & Qualified Opportunity Funds.  <a href="https://www.saul.com/capabilities/service/opportunity-zones-qualified-opportunity-funds">https://www.saul.com/capabilities/service/opportunity-zones-qualified-opportunity-funds</a>

<br>
    <br>U.S. Treasury Department. (2021). Use of the Opportunity Zone Tax Incentive.  <a href="https://home.treasury.gov/system/files/131/WP-123.pdf">https://home.treasury.gov/system/files/131/WP-123.pdf</a>


    </p>
                             <p><u><b>Legal Qualification Requirements</u></b>

<br>•	Eligible Location – The business or property must be located within a federally designated Qualified Opportunity Zone census tract.
<br>•	QOZB Status – Must meet the "Qualified Opportunity Zone Business" definition (70% asset test and 50% gross income test).
<br>•	Corporate Structure – The fund must be organized as a corporation or partnership for federal tax purposes.
<br>•	Asset Test Compliance – At least 90% of the fund’s assets must consist of OZ property, tested semi-annually.
<br>•	Substantial Improvement – Existing buildings must be improved by an amount exceeding the original purchase price within 30 months.
<br>•	Non-Sin Business – Cannot be a "sin business" (e.g., golf course, country club, massage parlor, liquor store, or gambling facility).
<br>•	IRS Self-Certification – The fund must file Form 8996 annually to certify it meets all QOF requirements.
<br>•	Active Conduct – The business must be actively engaged in a trade or business, not just passive investment (except for rental real estate).




    </p>

                                

    <p><b><u>Supporting Document List</u></b>
<br>•	IRS Form 8996 – The annual self-certification form for Qualified Opportunity Funds.
<br>•	IRS Form 8997 – The statement of QOF investments filed by the investor.
<br>•	QOZB Operating Agreement – Legal document outlining the business's commitment to OZ compliance.
<br>•	Census Tract Verification – Documentation (map/address) proving the property is in a designated zone.
<br>•	Asset Test Records – Semi-annual calculations proving the fund meets the 90% asset threshold.
<br>•	Improvement Budget/Timeline – Detailed plan showing how the "substantial improvement" requirement will be met.
<br>•	Gross Income Records – Evidence that at least 50% of income is derived from activities within the zone.
<br>•	Investment Subscription Agreement – Legal contract for investors reinvesting capital gains into the fund.
<br>•	Phase I Environmental Report – Often required for real estate OZ projects to ensure site safety.




    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def governmentincentivesopportunityzonefaq(request):
    introduction = mark_safe("""<p><b><center>Capital Market: Government Incentives<br>

    Opportunity Zone Tax Credit Fund</center></b></p>                       

    <p><center><u><b>Frequently Asked Question</u></b></center></p>

                            

    <p><u><b>1.	What is an Opportunity Zone Tax Credit Fund, and how does it differ from other funding options? </u></b><br>

    •Answer: An Opportunity Zone Tax Credit Fund is a government-backed program that provides tax incentives to investors who invest capital gains into designated low-income Opportunity Zones, encouraging economic development and long-term investments in underserved communities.
</p>

                            

     <p><u><b>2.	What types of businesses or projects are best suited for Opportunity Zone investment? </u></b><br>

    •Answer: Businesses or projects located within designated Opportunity Zones, including real estate development, small business expansion, infrastructure projects, and community improvement initiatives, are ideal candidates for investment.
</p>


                            

    <p><u><b>3.	How much investment can I make in an Opportunity Zone Tax Credit Fund? </u></b><br>

    •Answer: Investors can roll over eligible capital gains into an Opportunity Zone Fund, with no statutory maximum, though practical investment limits may depend on the size of the fund and project availability.
</p>


                            

   <p><u><b>4.	How quickly can I access the tax benefits after investing? </u></b><br>

    •Answer: Tax benefits are realized according to a multi-year schedule: a partial gain exclusion after 5 years, additional exclusion after 7 years, and full exclusion of gains on the Opportunity Zone investment if held for at least 10 years.
</p>


                            

    <p><u><b>5.	What are the costs associated with investing in an Opportunity Zone Fund? </u></b><br>

    •Answer: Costs include fund management fees, due diligence expenses, and potential investment risks, while upfront investment is the capital amount rolled over from eligible gains.
</p>


                            

   <p><u><b>6.	Do I have to give up equity in exchange for investing in an Opportunity Zone Fund? </u></b><br>

    •Answer: No direct equity is required; however, the investment usually takes the form of equity or debt in projects within Opportunity Zones, providing potential returns while securing tax incentives.
</p>


                            

 <p><u><b>7.	Can I invest in other opportunities while participating in an Opportunity Zone Fund? </u></b><br>

    •Answer: Yes, investors can participate in multiple funds or investments simultaneously, but must track eligible capital gains to ensure compliance with Opportunity Zone tax rules.
</p>
                            

     <p><u><b>8.	What are the key benefits of an Opportunity Zone Fund over traditional investments? </u></b><br>

    •Answer: Key benefits include deferral and potential reduction of capital gains taxes, long-term gain exclusion, economic impact on underserved communities, and potential investment returns from fund projects.
</p>

                            

   <p><u><b>9.	What resources and support can I expect from an Opportunity Zone Fund? </u></b><br>

    •Answer: Investors receive detailed fund reports, project updates, compliance guidance, and oversight from fund managers, along with access to investment opportunities vetted for eligibility.
</p>

                            

    <p><u><b>10.	What happens after the investment period ends? </u></b><br>

    •Answer: After holding the investment for at least 10 years, investors can sell the investment without paying taxes on the appreciation within the Opportunity Zone Fund, while complying with reporting and fund exit requirements.
</p>

                        

   <p><u><b>11.	Are there any risks associated with Opportunity Zone Fund investments? </u></b><br>

    •Answer: Risks include project underperformance, fund management fees, illiquidity, regulatory compliance issues, and the possibility that tax incentives may change.
</p>

                        

  <p><u><b>12.	How does an Opportunity Zone Fund compare to other government incentives or private investments? </u></b><br>

    •Answer: Opportunity Zone Funds combine tax deferral and exclusion benefits with targeted economic development, unlike standard private investments that do not offer tax incentives and traditional grants or loans that may have repayment or compliance requirements.
</p>

                        

   <p><u><b>13.	Can I invest in an Opportunity Zone Fund if I have already realized capital gains? </u></b><br>

    •Answer: Yes, the program is specifically designed for investors with eligible capital gains from prior investments, which can be rolled over into the fund for tax benefits.
</p>

                        

 <p><u><b>14.	What types of projects typically get approved for Opportunity Zone Fund investment? </u></b><br>

    •Answer: Projects that demonstrate economic impact, community development, job creation, real estate or business growth, and compliance with Opportunity Zone regulations are most likely to be approved.
</p>

                        

  <p><u><b>15.	How can I increase my chances of success with an Opportunity Zone Fund investment? </u></b><br>

    •Answer: Investors should perform due diligence, select experienced fund managers, align projects with regulatory guidelines, monitor investment performance, and hold investments for the required period to maximize tax benefits.
</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def governmentincentivesopportunityzonetwelve(request):
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

    Capital Type: Opportunity Zone Tax Credit Fund</p></center>

 

    <p><b><u>1 - Stage of Development Assessment</b></u><br>

Opportunity Zone (OZ) funding is best suited for growth-stage and expansion-stage businesses, particularly those involved in real estate or operating businesses within designated Opportunity Zones.
    </p>

   

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Eligible entities typically include C-Corps, LLCs, and partnerships, often structured as Qualified Opportunity Zone Businesses (QOZBs).

    </p>

   

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Businesses may have existing capital, but projects must meet Opportunity Zone qualification rules, including substantial improvement or active business requirements.

    </p>

 

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>

This capital operates in private equity markets, incentivized by federal tax policy. Prior equity investment is acceptable if compliance is maintained.
    </p>

 

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>

Investments typically range from $500,000 to tens of millions, depending on project scope and investor participation.
    </p>

   

    <p><b><u>6 - Capital Round Assessment</b></u><br>
OZ investments align with growth equity or expansion rounds, particularly for real estate or infrastructure-heavy projects.

    </p>

 

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>

Funding may be provided in single or milestone-based tranches, especially for development projects.
    </p>

   

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Funds must be used for qualified Opportunity Zone activities, such as:
<br>•	Property development or improvement
<br>•	Business expansion within the zone
<br>•	Use outside qualified purposes is restricted.


    
</p>

   

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk is moderate to high, due to regulatory compliance requirements, long investment horizons, and project execution risk.

    </p>

 

    <p><b><u>10 - Capital Cost Assessment</b></u><br>

Cost of capital involves equity dilution, but is offset by significant tax deferral and exclusion benefits for investors.
    </p>

   

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>

Upfront costs are moderate, including legal structuring, compliance, and fund administration expenses.
    </p>

 

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>

Capital deployment typically occurs within 2–6 months, depending on fund structure, investor commitments, and regulatory compliance.
</p>
"""

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)