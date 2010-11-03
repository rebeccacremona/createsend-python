import unittest

from createsend import Client

class CreateSendTestCase(unittest.TestCase):

  def setUp(self):
    self.cl = Client()

  def test_create(self):
    self.cl.stub_request("create_client.json")
    client_id = self.cl.create("Client Company Name", "Client Contact Name", "client@example.com", "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")
    self.assertEquals("32a381c49a2df99f1d0c6f3c112352b9", client_id)

  def test_details(self):
    self.cl.stub_request("client_details.json")
    cl = self.cl.details()
    self.assertEquals(cl.BasicDetails.ClientID, "4a397ccaaa55eb4e6aa1221e1e2d7122")
    self.assertEquals(cl.BasicDetails.ContactName, "Client One (contact)")
    self.assertEquals(cl.AccessDetails.Username, "clientone")
    self.assertEquals(cl.AccessDetails.AccessLevel, 23)
  
  def test_campaigns(self):
    self.cl.stub_request("campaigns.json")
    campaigns = self.cl.campaigns()
    self.assertEquals(len(campaigns), 2)
    self.assertEquals(campaigns[0].CampaignID, 'fc0ce7105baeaf97f47c99be31d02a91')
    self.assertEquals(campaigns[0].WebVersionURL, 'http://hello.createsend.com/t/ViewEmail/r/765E86829575EE2C/C67FD2F38AC4859C/')
    self.assertEquals(campaigns[0].Subject, 'Campaign One')
    self.assertEquals(campaigns[0].Name, 'Campaign One')
    self.assertEquals(campaigns[0].SentDate, '2010-10-12 12:58:00')
    self.assertEquals(campaigns[0].TotalRecipients, 2245)

  def test_drafts(self):
    self.cl.stub_request("drafts.json")
    drafts = self.cl.drafts()
    self.assertEquals(len(drafts), 2)
    self.assertEquals(drafts[0].CampaignID, '7c7424792065d92627139208c8c01db1')
    self.assertEquals(drafts[0].Name, 'Draft One')
    self.assertEquals(drafts[0].Subject, 'Draft One')
    self.assertEquals(drafts[0].DateCreated, '2010-08-19 16:08:00')
    self.assertEquals(drafts[0].PreviewURL, 'http://hello.createsend.com/t/ViewEmail/r/E97A7BB2E6983DA1/C67FD2F38AC4859C/')

  def test_lists(self):
    self.cl.stub_request("lists.json")
    lists = self.cl.lists()
    self.assertEquals(len(lists), 2)
    self.assertEquals(lists[0].ListID, 'a58ee1d3039b8bec838e6d1482a8a965')
    self.assertEquals(lists[0].Name, 'List One')
    
  def test_segments(self):
    self.cl.stub_request("segments.json")
    segments = self.cl.lists()
    self.assertEquals(len(segments), 2)
    self.assertEquals(segments[0].ListID, 'a58ee1d3039b8bec838e6d1482a8a965')
    self.assertEquals(segments[0].SegmentID, '46aa5e01fd43381863d4e42cf277d3a9')
    self.assertEquals(segments[0].Title, 'Segment One')

  def test_suppressoinlist(self):
    self.cl.stub_request("suppressionlist.json")
    res = self.cl.suppressionlist()
    self.assertEquals(res.ResultsOrderedBy, "email")
    self.assertEquals(res.OrderDirection, "asc")
    self.assertEquals(res.PageNumber, 1)
    self.assertEquals(res.PageSize, 1000)
    self.assertEquals(res.RecordsOnThisPage, 5)
    self.assertEquals(res.TotalNumberOfRecords, 5)
    self.assertEquals(res.NumberOfPages, 1)
    self.assertEquals(len(res.Results), 5)
    self.assertEquals(res.Results[0].EmailAddress, "example+1@example.com")
    self.assertEquals(res.Results[0].Date, "2010-10-26 10:55:31")
    self.assertEquals(res.Results[0].State, "Suppressed")
