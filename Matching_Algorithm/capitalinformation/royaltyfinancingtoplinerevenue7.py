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


def royaltyfinancingtoplinerevenue(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""<p><center><b><u>Definition of Capital Market: Royalty Financing</b></u><br>

    Capital Type: Top Line Revenue </center></p>

    <p><b><u>Introduction</u></b><br>

Royalty financing is an alternative funding model in which investors provide capital to a business in exchange for a fixed percentage of the company’s top-line revenue until a predetermined return multiple is reached. Unlike equity financing, royalty financing does not involve ownership dilution, and unlike traditional debt, repayments are tied directly to revenue performance. {n} fits that definition.
Royalty financing has gained traction among startups and growth-stage companies seeking flexible, non-dilutive capital, particularly in sectors with predictable revenue streams. On average, royalty agreements require businesses to pay between 2% and 10% of gross revenue until investors receive 1.5x to 3x their original investment. This model aligns investor returns with company performance while reducing fixed repayment pressure during low-revenue periods (Royalty Exchange, 2023).
    </p>

 

    <p><b><u>Definition of Capital Type</b></u><br>

    <br>1.	Royalty financing, also known as revenue-based financing, is a capital structure where businesses receive upfront funding and agree to repay investors through a percentage of ongoing gross revenues. Payments fluctuate with business performance and continue until the agreed return cap is achieved. This structure avoids equity dilution and does not require fixed repayment schedules typical of traditional loans (Investopedia, n.d.).

<br>



    <br>2.	Royalty financing is best suited for companies with consistent and predictable revenue streams, strong gross margins, and proven product-market fit. These typically include SaaS companies, consumer brands, subscription-based businesses, and intellectual property–driven enterprises. Businesses at the post-revenue or early growth stage benefit most, as stable revenue enables reliable repayment without compromising operational cash flow (Earnest Capital, 2022).

<br>


    <br>3.	Royalty-based funding originated in the natural resource and entertainment industries, where royalties were paid on extraction or content sales. Over time, the model expanded into startup finance as investors sought alternatives to equity-heavy venture capital. In recent years, revenue-based financing has gained prominence due to founder demand for non-dilutive capital and investor interest in predictable cash-flow returns, particularly in technology and consumer sectors (Gompers et al., 2020).

<br>

    <br>4.	Despite its flexibility, royalty financing presents certain limitations. Revenue sharing reduces available cash flow during high-growth periods, potentially slowing reinvestment. The total repayment amount may exceed traditional debt costs if revenue grows rapidly. Additionally, royalty agreements can be complex and require careful negotiation to avoid restrictive terms that limit future fundraising or operational decisions (CB Insights, 2023).

<br>

    <br>5.	To secure royalty financing, a company must demonstrate stable revenue, strong unit economics, and reliable financial reporting. Investors evaluate revenue consistency, customer retention, and margin sustainability before determining royalty rates and return caps. Agreements specify payment percentages, duration, reporting obligations, and buyout options. Transparent financial disclosures and legal documentation are critical to successful execution.
    </p>

                            

    <p><u><b>References</u></b><br>

  <br>Investopedia. (n.d.). Revenue-based financing.  <a href="https://www.investopedia.com">https://www.investopedia.com</a>

<br>  
  <br>Royalty Exchange. (2023). How royalty financing works. <a href="https://www.royaltyexchange.com">https://www.royaltyexchange.com</a>

<br>

     <br>Earnest Capital. (2022). Revenue-based financing explained. <a href="https://earnestcapital.com ">https://earnestcapital.com </a>

<br>

   <br>Gompers, P., et al. (2020). Venture capital and alternative finance. Journal of Finance. <a href="https://econpapers.repec.org/article/eeejfinec/v_3a135_3ay_3a2020_3ai_3a1_3ap_3a169-190.htm ">https://econpapers.repec.org/article/eeejfinec/v_3a135_3ay_3a2020_3ai_3a1_3ap_3a169-190.htm </a>

<br>

   <br>CB Insights. (2023). Alternative startup financing models.  <a href="https://www.cbinsights.com">https://www.cbinsights.com</a>

<br>

 


    </p>

                                                          

    <p><u><b>Legal Qualification Requirements</u></b>

<br>•	Registered revenue-generating business
<br>•	Minimum revenue thresholds
<br>•	Verified financial statements
<br>•	No existing revenue liens
<br>•	Legal authority to enter royalty agreements
<br>•	Compliance with tax and reporting regulations




    </p>

                                

    <p><b><u>Supporting Document List</u></b>
<br>•	Revenue statements
<br>•	Bank transaction records
<br>•	Financial projections
<br>•	Royalty agreement draft
<br>•	Legal incorporation documents
<br>•	Customer contracts or subscription data




    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def royaltyfinancingtoplinerevenuefaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Royalty Financing<br>

    Top Line Revenue</center></b></p>                       

    <p><center><u><b>Frequently Asked Question</u></b></center></p>

                            

    <p><u><b>1. What is royalty financing based on top-line revenue?</u></b><br>

    •Answer: Royalty financing is a funding method where a business receives upfront capital in exchange for agreeing to pay a fixed percentage of its top-line revenue (gross sales) over time until a predefined repayment cap is reached.
</p>

                            

     <p><u><b>2. How does royalty financing differ from equity financing?</u></b><br>

    •Answer: Royalty financing does not involve giving up ownership or control. Instead of equity dilution, the business repays investors through revenue-based payments. Once the agreed repayment cap is met, the obligation ends.
</p>


                            

    <p><u><b>3. How does royalty financing differ from traditional debt or loans?</u></b><br>

    •Answer: Unlike fixed loan repayments, royalty payments fluctuate with revenue. When revenue is low, payments decrease; when revenue is high, payments increase. There is usually no fixed maturity date or personal collateral requirement.
</p>


                            

   <p><u><b>4. What types of businesses are best suited for royalty financing?</u></b><br>

    •Answer: Royalty financing is best suited for businesses with predictable and recurring revenue, such as SaaS, consumer products, licensing-based companies, healthcare, education services, and established SMEs with steady sales.
</p>


                            

    <p><u><b>5. Is royalty financing suitable for pre-revenue startups?</u></b><br>

    •Answer: Generally, no. Because repayments are tied to revenue, most royalty financiers require existing revenue. Early-revenue or growth-stage companies are better candidates than idea-stage startups.
</p>


                            

   <p><u><b>6. How much capital can be raised through royalty financing?</u></b><br>

    •Answer: The amount depends on current revenue levels, growth rate, and margins. Funding is typically a multiple of monthly or annual revenue, with repayment caps commonly ranging from 1.3× to 3× the invested amount.
</p>


                            

 <p><u><b>7. How quickly can businesses access royalty financing?</u></b><br>

    •Answer: Once financials are reviewed and terms agreed, capital can often be accessed faster than traditional bank loans, sometimes within a few weeks, depending on due diligence requirements.
</p>
                            

     <p><u><b>8. Do royalty financiers take equity or control rights?</u></b><br>

    •Answer: No. Royalty financiers typically do not take equity, board seats, or voting rights. Their return is purely tied to revenue performance.
</p>

                            

   <p><u><b>9. How are royalty payments calculated and made?</u></b><br>

    •Answer: Payments are calculated as a fixed percentage of gross revenue (top-line), often between 2% and 10%. Payments are usually made monthly or quarterly until the total repayment cap is reached.
</p>

                            

    <p><u><b>10. What happens if revenue declines or stops?</u></b><br>

    •Answer: If revenue declines, royalty payments automatically decrease. If revenue stops, payments pause. This flexibility reduces cash-flow pressure compared to fixed loan repayments.
</p>

                        

   <p><u><b>11. What are the key benefits of royalty financing?</u></b><br>

    •Answer: Key benefits include no equity dilution, flexible repayments, alignment with business performance, faster access to capital, and founder control retention.
</p>

                        

  <p><u><b>12. What are the risks or limitations of royalty financing?</u></b><br>

    •Answer: Risks include higher total repayment cost compared to traditional debt and reduced cash flow during high-revenue periods. It may also be unsuitable for businesses with thin margins.
</p>

                        

   <p><u><b>13. Can royalty financing be combined with other funding sources?</u></b><br>

    •Answer: Yes. Royalty financing can be combined with equity, grants, accelerators, or bank loans, as long as revenue-sharing obligations do not conflict with other agreements.
</p>

                        

 <p><u><b>14. How does royalty financing compare to venture capital?</u></b><br>

    •Answer: Venture capital focuses on high growth and equity returns, while royalty financing focuses on revenue performance and predictable returns. Royalty financing is more founder-friendly for businesses that want growth without ownership dilution.
</p>

                        

  <p><u><b>15. How can a business improve its chances of securing royalty financing?</u></b><br>

    •Answer: Businesses should demonstrate consistent revenue, strong margins, transparent financial reporting, and a clear growth strategy. Predictability and scalability significantly improve approval chances.
</p>                         
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def royaltyfinancingtoplinerevenuetwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Royalty Financing</b></u><br>

    Capital Type: Top Line Revenue</p></center>

 

    <p><b><u>1 - Stage of Development Assessment</b></u><br>

Royalty financing is best suited for early-revenue to growth-stage businesses that have a proven product or service and predictable, recurring revenue. It is not suitable for idea-stage or pre-revenue startups, as repayments are directly linked to revenue generation.
    </p>

   

    <p><b><u>2 - Entity Type Assessment</b></u><br>

Royalty financing is compatible with most formal business entities, including sole proprietorships, partnerships, LLCs, and corporations. Investors focus more on revenue stability and margins than on the legal structure of the business.
    </p>

   

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Businesses seeking royalty financing are expected to have existing revenue streams and some operational history. Prior bootstrapping, grants, or even equity funding is acceptable, provided the company’s revenue can comfortably support royalty payments.

    </p>

 

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Royalty financing operates outside traditional equity markets. Previous venture capital or angel investment does not automatically disqualify a business, but investors closely assess whether existing obligations or dilution structures interfere with revenue-sharing agreements.

    </p>

 

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>

The amount of capital raised through royalty financing is typically moderate, often tied to a multiple of current annual revenue. It is commonly used for growth initiatives, such as marketing expansion, product scaling, or entering new markets rather than large capital-intensive projects.
    </p>

   

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Royalty financing does not align with traditional startup funding rounds (pre-seed, seed, Series A). Instead, it fits into a revenue-growth financing stage, often positioned between early equity funding and traditional bank loans.

    </p>

 

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funding is usually provided in a single upfront tranche. Repayment occurs through ongoing royalty payments, calculated as a fixed percentage of top-line revenue until a predetermined return cap is reached.

    </p>

   

    <p><b><u>8 - Use of Funds Assessment</b></u><br>

Funds raised through royalty financing are typically used for:
<br>•	Marketing and customer acquisition
<br>•	Sales expansion
<br>•	Inventory or production scaling
<br>•	Working capital needs
Use of funds is generally flexible, but investors expect capital to be deployed in activities that directly increase revenue, as repayments depend on top-line performance.

    
</p>

   

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk is shared between the business and the investor. If revenue declines, royalty payments decrease, reducing short-term pressure on the business. However, consistently strong revenue can result in higher total repayment compared to fixed-interest debt.

    </p>

 

    <p><b><u>10 - Capital Cost Assessment</b></u><br>

The cost of capital is variable rather than fixed. Instead of interest or equity dilution, the business commits a percentage of revenue (e.g., 3–10%) until a repayment multiple (e.g., 1.3x–2.5x) is met. This can be cost-effective or expensive depending on growth performance.
    </p>

   

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are moderate and may include legal fees, due diligence costs, and structuring fees. There is usually no equity dilution and no collateral requirement, which reduces long-term ownership cost.

    </p>

 

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>

Royalty financing offers a relatively fast path to capital, typically 2–6 weeks, depending on revenue verification and contract negotiation. This makes it faster than traditional bank loans but slower than owner-funded capital.
</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)