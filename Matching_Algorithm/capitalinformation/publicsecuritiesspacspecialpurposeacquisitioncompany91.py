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

def publicsecuritiesspacspecialpurposeacquisitioncompany(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Public Securities</b></u><br>
    Capital Type: SPAC - Special Purpose Acquisition Company</center></p>
    <p><b><u>Introduction</u></b><br>
    A Special Purpose Acquisition Company (SPAC) is a publicly traded shell company created solely for the purpose of raising capital through an initial public offering (IPO) to acquire or merge with an existing private company within a specified time period. {n} fits that definition. SPACs have gained popularity as an alternative route to public markets for private companies seeking faster access to liquidity compared to traditional IPO processes. After raising capital, the SPAC places the funds in a trust account until a suitable acquisition target is identified. In the United States, SPAC offerings are regulated by the U.S. Securities and Exchange Commission under federal securities laws, and SPAC sponsors typically receive equity incentives for successful acquisitions. The SPAC model surged in popularity between 2020 and 2021, raising over $160 billion globally during the peak market period.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. A SPAC is a publicly listed acquisition vehicle that raises funds from investors with the intention of acquiring or merging with a private operating company. Investors purchase SPAC units, which usually consist of common shares and warrants. After the IPO, the SPAC management team searches for a target company to complete a business combination, commonly called a de-SPAC transaction. If the SPAC fails to complete an acquisition within the regulatory deadline (usually 18–24 months), the capital is returned to investors (SEC, 2023).<br>
    <br>
    2. SPAC mergers are best suited for private companies seeking faster public market entry without undergoing the lengthy traditional IPO process. Technology startups, high-growth enterprises, and companies with strong projected future earnings often use SPAC mergers as an alternative listing method. However, companies must demonstrate credible financial forecasts and operational readiness to satisfy institutional investors.<br>
    <br>
    3. The SPAC concept dates back to the 1990s but gained significant popularity in the 2020 global capital market expansion. SPAC structures evolved as an alternative to traditional IPOs, allowing private companies to merge into already publicly listed entities. The regulatory environment was strengthened following market concerns regarding valuation transparency and disclosure quality. The Securities Act of 1933 and related disclosure regulations apply to SPAC transactions.<br>
    <br>
    4. SPAC investments carry market volatility risk, valuation uncertainty, and sponsor incentive conflicts. If acquisition targets fail to meet investor expectations, share prices may decline after the merger. SPAC performance historically shows high initial enthusiasm followed by post-merger price corrections. Additionally, regulatory scrutiny has increased regarding forward-looking projections and disclosure quality.<br>
    <br>
    5. To participate in SPAC transactions, sponsors must establish a SPAC entity, conduct an IPO to raise capital, and place proceeds into a trust account. Successful SPAC mergers depend on identifying high-quality acquisition targets, maintaining transparent disclosure standards, securing shareholder approval, and completing the business combination within the regulatory timeframe.
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Registration with the U.S. Securities and Exchange Commission<br>
    · Compliance with the Securities Act of 1933<br>
    · SPAC Trust Account Requirement<br>
    · Shareholder Approval for Acquisition<br>
    · Disclosure of Sponsor Compensation<br>
    · AML/KYC Compliance<br>
    · Merger Agreement Execution
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    · SPAC IPO Prospectus<br>
    · Business Combination Agreement<br>
    · Financial Statements (Audited)<br>
    · Sponsor Agreement<br>
    · Trust Account Documentation<br>
    · Risk Disclosure Statement<br>
    · Target Company Due Diligence Report<br>
    · Shareholder Voting Materials
    </p>
    <p><u><b>References</b></u><br>
    1. U.S. Securities and Exchange Commission. (2023). Special Purpose Acquisition Companies (SPACs). https://www.sec.gov/spotlight/spac<br>
    2. Investopedia. (n.d.). SPAC Definition and Structure. https://www.investopedia.com/terms/s/spac.asp<br>
    3. Securities Act of 1933. (1933). https://www.sec.gov/about/laws/sa33.pdf<br>
    4. Harvard Law School Forum on Corporate Governance. (2021). SPAC Market Trends and Risks. https://corpgov.law.harvard.edu<br>
    5. McKinsey & Company. (2021). The rise of SPAC transactions. https://www.mckinsey.com
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def publicsecuritiesspacspecialpurposeacquisitioncompanyfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Public Securities<br>
    SPAC - Special Purpose Acquisition Company</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is a SPAC?</u></b><br>
    • Answer: A Special Purpose Acquisition Company (SPAC) is a publicly traded company created solely to raise capital through an IPO for the purpose of acquiring an existing private company.
    </p>
    <p><u><b>2. How does a SPAC work?</u></b><br>
    • Answer: A SPAC raises funds through an IPO, places the proceeds in a trust account, and later uses the capital to acquire or merge with a target company.
    </p>
    <p><u><b>3. Who manages a SPAC?</u></b><br>
    • Answer: SPACs are managed by a sponsor team, typically experienced investors or industry executives who identify and acquire target companies.
    </p>
    <p><u><b>4. What happens after a SPAC raises capital?</u></b><br>
    • Answer: The SPAC searches for a suitable acquisition target, usually within 18 to 24 months, or returns capital to investors if no acquisition is completed.
    </p>
    <p><u><b>5. What do investors receive in a SPAC?</u></b><br>
    • Answer: Investors typically receive units consisting of common shares and warrants, allowing participation in potential future value growth.
    </p>
    <p><u><b>6. What are SPAC warrants?</u></b><br>
    • Answer: SPAC warrants are securities that give investors the right to purchase additional shares at a predetermined price in the future.
    </p>
    <p><u><b>7. What are the advantages of SPACs?</u></b><br>
    • Answer: Advantages include faster access to public markets, reduced IPO complexity, and access to experienced sponsor management.
    </p>
    <p><u><b>8. What are the risks of investing in SPACs?</u></b><br>
    • Answer: Risks include target acquisition failure, market volatility, dilution from warrants, and uncertain post-merger performance.
    </p>
    <p><u><b>9. How are SPACs regulated?</u></b><br>
    • Answer: SPACs are regulated by securities authorities such as the SEC and must comply with public company disclosure requirements.
    </p>
    <p><u><b>10. How long does a SPAC have to complete an acquisition?</u></b><br>
    • Answer: SPACs typically have 18 to 24 months to complete a business combination after the IPO.
    </p>
    <p><u><b>11. What happens if a SPAC fails to find a target?</u></b><br>
    • Answer: If no acquisition occurs within the specified period, the SPAC liquidates and returns funds to investors.
    </p>
    <p><u><b>12. Do SPACs cause shareholder dilution?</u></b><br>
    • Answer: Yes, dilution can occur due to sponsor shares, warrants, and transaction structuring.
    </p>
    <p><u><b>13. How does a SPAC differ from a traditional IPO?</u></b><br>
    • Answer: A SPAC is a merger-based path to public listing, while a traditional IPO involves direct public offering of company shares.
    </p>
    <p><u><b>14. Who should consider SPAC financing?</u></b><br>
    • Answer: Growth-stage companies seeking faster public market access and flexible negotiation structures may consider SPAC mergers.
    </p>
    <p><u><b>15. When are SPACs commonly used?</u></b><br>
    • Answer: SPACs are commonly used when private companies want to go public without undergoing the lengthy traditional IPO process.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def publicsecuritiesspacspecialpurposeacquisitioncompanytwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Public Securities</b></u><br>
    Capital Type: SPAC - Special Purpose Acquisition Company</p></center>
    <p><b><u>1 - Stage of Development Assessment</u></b><br>
    A SPAC is best suited for late-stage private companies seeking a faster public market entry without undergoing the traditional IPO process. Target companies are usually growth-stage or mature businesses with established operations and revenue visibility.
    </p>
    <p><b><u>2 - Entity Type Assessment</u></b><br>
    SPACs are formed as C-Corporations and are created specifically for the purpose of raising public capital to acquire or merge with a target operating company.
    SPAC structures are regulated under public market securities laws enforced by the U.S. Securities and Exchange Commission.
    </p>
    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    Before SPAC participation, target companies typically demonstrate:<br>
    · Audited financial statements<br>
    · Strong business model validation<br>
    · Institutional growth potential<br>
    · Readiness for public market reporting<br>
    SPAC sponsors usually raise initial capital before identifying acquisition targets.
    </p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    SPACs operate in the public securities market.
    Capital is initially raised through public share issuance on exchanges such as New York Stock Exchange or Nasdaq.
    </p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    Typical SPAC IPO raises range from $100 million to $1 billion+, depending on sponsor reputation and market conditions.
    </p>
    <p><b><u>6 - Capital Round Assessment</u></b><br>
    SPAC capital is raised in two phases:<br>
    · Initial SPAC IPO funding (blank-check capital pool)<br>
    · Subsequent merger financing when a target company is acquired<br>
    Investors initially purchase SPAC shares and may redeem them before the acquisition closes.
    </p>
    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    Capital is usually raised in:<br>
    · One public IPO tranche for the SPAC trust account<br>
    · Additional PIPE financing (Private Investment in Public Equity) may follow during the merger transaction<br>
    Funds are held in trust until acquisition approval.
    </p>
    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    Funds are primarily used for:<br>
    · Acquisition of a target operating company<br>
    · Transaction advisory fees<br>
    · Legal and merger execution costs<br>
    · Post-merger integration capital<br>
    Sponsor shares and transaction expenses are typically separate from trust capital.
    </p>
    <p><b><u>9 - Risk Assessment</u></b><br>
    Risk level is high.
    Key risks include:<br>
    · Failure to identify or close acquisition targets<br>
    · Redemption risk from shareholders<br>
    · Market sentiment volatility<br>
    · Post-merger performance uncertainty<br>
    · Regulatory scrutiny<br>
    Many SPACs historically underperformed post-merger.
    </p>
    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    Cost of capital includes:<br>
    · Sponsor promote equity (often ~20% founder share)<br>
    · Underwriting fees (5%–7%)<br>
    · PIPE financing costs<br>
    · Shareholder redemption dilution<br>
    Effective capital cost can be significant.
    </p>
    <p><b><u>11 - Up Front Cost Assessment</u></b><br>
    Upfront costs are very high, including:<br>
    · Legal and regulatory compliance<br>
    · Underwriter fees<br>
    · Exchange listing expenses<br>
    · Audit and accounting preparation<br>
    · Sponsor structuring costs<br>
    SPAC formation can require millions in preparation capital.
    </p>
    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
    Timing is moderate, typically:<br>
    · SPAC IPO launch: 3–6 months<br>
    · Target acquisition identification: 6–24 months<br>
    If acquisition fails within the specified period, the SPAC must liquidate and return funds to investors.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
