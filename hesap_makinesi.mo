actor hesap_makinesi{
    var hucre: Int = 0;

    //Toplama
    public func toplama(sayi: Int) : async Int{
        hucre += sayi;
        hucre 
    };
     //Çıkarma
    public func cikarma(sayi: Int) : async Int{
        hucre -= sayi;
        hucre 
    };
     //Çarpma
    public func carpma(sayi: Int) : async Int{
        hucre *= sayi;
        hucre 
    };
     //Bölme
    public func bolme(sayi: Int) : async ?Int{
        if(sayi == 0){
            null
        }
        else{
            hucre /= sayi;
            ?hucre 
        }
    };

    //Temizleme
    public func temizle():  async (){
        hucre := 0;
    };

};